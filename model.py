
import random
from mesa import Model
from mesa.space import MultiGrid
from mesa.time import SimultaneousActivation
from agent import CarAgent, ParkingLotAgent, BuildingAgent, SemaphoreAgent, AggressiveDriver, CautiousDriver, DistractedDriver, LearningDriver
from map import Parkings, Buildings, Semaphores
from completeMap import OptionMap
from aStar import create_maximal_graph, astarComplete, manhattan_distance
from mesa.datacollection import DataCollector


class TrafficModel(Model):

    def create_car_agents(self):
        # Clear existing car agents
        for agent in list(self.schedule.agents):
            if isinstance(agent, CarAgent):
                self.grid.remove_agent(agent)
                self.schedule.remove(agent)

        # Debug: Check number of car agents before creation
        print(f"DEBUG: Number of CarAgents before creation: {len([a for a in self.schedule.agents if isinstance(a, CarAgent)])}")

        # Create new car agents
        driver_classes = [AggressiveDriver, CautiousDriver, DistractedDriver, LearningDriver]
        options = Parkings
        for _ in range(self.num_cars):
            starting_pos = random.choice(options)
            target_pos = random.choice(Parkings)
            while starting_pos == target_pos:
                starting_pos = random.choice(options)
            path = astarComplete(self.G, starting_pos, target_pos, manhattan_distance)
            car_type = random.choice(driver_classes)
            c = car_type(self.ids, self, starting_pos, target_pos, path)
            self.ids += 1
            self.schedule.add(c)
            self.grid.place_agent(c, starting_pos)

        # Debug: Check number of car agents after creation
        print(f"DEBUG: Number of CarAgents after creation: {len([a for a in self.schedule.agents if isinstance(a, CarAgent)])}")


    def __init__(self, width, height, n_cars):
        super().__init__()  # Make sure to call the parent constructor
        self.G = create_maximal_graph(OptionMap)
        self.num_cars = n_cars
        self.completedCars = 0
        self.grid = MultiGrid(width, height, True)
        self.schedule = SimultaneousActivation(self)
        self.ids = 1
        self.running = True  # Add this line to set the simulation as running
        self.messages = []

        self.jammed_encounters = {
            "AggressiveDriver": 0,
            "CautiousDriver": 0,
            "DistractedDriver": 0,
            "LearningDriver": 0
        }
        
        self.datacollector = DataCollector(
            model_reporters={
                "Aggressive Advances": lambda m: sum(a.steps_taken for a in m.schedule.agents if isinstance(a, AggressiveDriver)),
                "Cautious Advances": lambda m: sum(a.steps_taken for a in m.schedule.agents if isinstance(a, CautiousDriver)),
                "Distracted Advances": lambda m: sum(a.steps_taken for a in m.schedule.agents if isinstance(a, DistractedDriver)),
                "Learning Advances": lambda m: sum(a.steps_taken for a in m.schedule.agents if isinstance(a, LearningDriver)),
                "Jammed Encounters": lambda m: m.jammed_encounters.copy()
            }
        )

        

        # Semaphore agents
        for data in Semaphores:
            coord, state = data
            s = SemaphoreAgent(self.ids, self, coord, state)
            self.ids += 1
            self.schedule.add(s)
            self.grid.place_agent(s, coord)

        # Parking Lot agents
        for coord in Parkings:
            pl = ParkingLotAgent(self.ids, self, coord)
            self.ids += 1
            self.schedule.add(pl)
            self.grid.place_agent(pl, coord)

        # Building agents
        for data in Buildings:
            coord, color = data
            b = BuildingAgent(self.ids, self, coord, color)
            self.ids += 1
            self.schedule.add(b)
            self.grid.place_agent(b, coord)

        # Create car agents
        self.create_car_agents()


    def check_jams(self):
        """Update jammed encounter statistics."""
        agent_positions = {}
        for agent in self.schedule.agents:
            if isinstance(agent, CarAgent):
                if agent.pos not in agent_positions:
                    agent_positions[agent.pos] = []
                agent_positions[agent.pos].append(agent)

        for pos, agents in agent_positions.items():
            if len(agents) > 1:  # Jam occurs when multiple agents are at the same position
                for agent in agents:
                    if isinstance(agent, AggressiveDriver):
                        self.jammed_encounters["AggressiveDriver"] += 1
                    elif isinstance(agent, CautiousDriver):
                        self.jammed_encounters["CautiousDriver"] += 1
                    elif isinstance(agent, DistractedDriver):
                        self.jammed_encounters["DistractedDriver"] += 1
                    elif isinstance(agent, LearningDriver):
                        self.jammed_encounters["LearningDriver"] += 1

    def step(self):
        try:
            self.schedule.step()  # Step all agents
            self.check_jams()
            self.datacollector.collect(self)

            # Remove completed car agents
            for agent in list(self.schedule.agents):
                if isinstance(agent, CarAgent) and agent.reached_goal and agent.stay_counter >= agent.stay_duration:
                    self.grid.remove_agent(agent)
                    self.schedule.remove(agent)
                    self.completedCars += 1

            # Re-create car agents if all have reached their goals
            if self.completedCars == self.num_cars:
                self.create_car_agents()
                self.completedCars = 0

            # Debug: Log the number of car agents
            print(f"DEBUG: Number of CarAgents in step: {len([a for a in self.schedule.agents if isinstance(a, CarAgent)])}")

            # Stop the simulation if no active car agents are left
            if not any(isinstance(agent, CarAgent) for agent in self.schedule.agents):
                self.running = False

            self.clear_messages()

        except Exception as e:
            print(f"An error occurred: {e}")



    def getInitialCarState(self):
        carPositions = []
        for agent in self.schedule.agents:
            if isinstance(agent, CarAgent):
                id = agent.unique_id
                x_coord, y_coord = agent.pos
                carPositions.append([id, x_coord, y_coord])
        return sorted(carPositions, key= lambda x: x[0])

    def getCarState(self):
        carPositions = []
        for agent in self.schedule.agents:
            if isinstance(agent, CarAgent):
                id = agent.unique_id
                x1_coord, y1_coord = agent.pos
                try:
                    x2_coord, y2_coord = agent.path[0]
                except IndexError:
                    x2_coord, y2_coord = agent.pos
                try:
                    x3_coord, y3_coord = agent.path[1]
                except IndexError:
                    x3_coord, y3_coord = x2_coord, y2_coord
                carPositions.append([id, x1_coord, y1_coord, x2_coord, y2_coord, x3_coord, y3_coord])
        return sorted(carPositions, key= lambda x: x[0])

    def getSemaphoreState(self):
        carLights = []
        for agent in self.schedule.agents:
            if isinstance(agent, SemaphoreAgent):
                id = agent.unique_id
                pos = agent.pos
                state = agent.state
                carLights.append([id, pos, state])
        return sorted(carLights, key= lambda x: x[0])
    
    def clear_messages(self):
        """Clear messages at the end of each step."""
        self.messages = []