import math
from mesa import Agent
import random
from map import Parkings
from aStar import astarComplete, manhattan_distance

class CarAgent(Agent):
    def __init__(self, unique_id, model, pos, t_pos, path):
        super().__init__(unique_id, model)
        self.pos = pos
        self.target_pos = t_pos
        self.path = path
        self.steps_taken = 0
        self.rotationToPos = 0
        self.jammedCounter = 0
        self.reached_goal = False
        self.stay_counter = 0
        self.stay_duration = 1

    def recalculateNewPath(self):
        new_target_pos = random.choice(Parkings)
        while new_target_pos == self.target_pos:
            new_target_pos = random.choice(Parkings)
        self.target_pos = new_target_pos
        new_path = astarComplete(self.model.G, self.pos, self.target_pos, manhattan_distance)
        if new_path:
            self.path = new_path
            self.jammedCounter = 0
        else:
            print(f"Agent {self.unique_id} failed to find a path. Retrying...")
            self.recalculateNewPath()

    def move(self):
        if self.reached_goal:
            self.stay_counter += 1
            return 
        if not self.path:
            if self.pos == self.target_pos:  # Ensure the agent is at the target
                self.reached_goal = True
            else:
                print(f"Agent {self.unique_id} is not at the target but has no path.")
                self.recalculateNewPath()  # Generate a new path to the target
            return

        # If the car has been in a jam for 5 steps, recalculate the path to a new target Parking
        if self.jammedCounter >= 5:
            self.recalculateNewPath()

        target_coordinates = self.path[0]
        cell_contents = self.model.grid.get_cell_list_contents([target_coordinates])
        # checks for semaphores
        traffic_lights = [obj for obj in cell_contents if isinstance(obj, SemaphoreAgent)]
        # checks for other cars
        other_cars = [obj for obj in cell_contents if isinstance(obj, CarAgent) and obj != self]

        if not traffic_lights or traffic_lights[0].state == "green":
            # Move only if there are no traffic lights or the traffic light is green
            if not other_cars:
                # Move only if the target cell is not occupied by another car
                self.model.grid.move_agent(self, target_coordinates)
                self.pos = target_coordinates
                self.path.pop(0)
                # If the car is not jammed, then the jammedCounter is reset
                self.jammedCounter = 0
            # If there is a car, then is jammed and the jammedCounter is increased
            else:
                self.jammedCounter += 1

    def step(self):
        if not self.reached_goal:
            self.steps_taken += 1
            self.move()
            if self.path:
                next_pos = self.path.pop(0)
                self.model.grid.move_agent(self, next_pos)
            if self.pos == self.target_pos: 
                self.reached_goal = True
        else:
            self.stay_counter += 1
        self.broadcast_intention()
        self.react_to_messages()
        

    def reached_final_position(self):
        return not bool(self.path)
    
    def broadcast_intention(self):
        """Broadcast current intention to the model's message queue."""
        self.model.messages.append({
            "agent_id": self.unique_id,
            "pos": self.pos,
            "intention": "moving" if self.path else "stopping",
            "priority": "normal",  # Priority can be adjusted based on agent type
        })

    def react_to_messages(self):
        """React to messages from other agents."""

        if not self.path:  # Skip if there's no path to react to
            return

        for message in self.model.messages:
            if message["agent_id"] == self.unique_id:
                continue  # Ignore own messages
            if "pos" in message and message["pos"] == self.path[0]:  # Potential conflict
                if message["priority"] == "normal":
                    self.jammedCounter += 1
                    return  # Stop moving this turn
    

class AggressiveDriver(CarAgent):
    def move(self):
        if not self.path:
            if self.pos == self.target_pos:  # Ensure the agent is at the target
                self.reached_goal = True
            else:
                print(f"Agent {self.unique_id} is not at the target but has no path.")
                self.recalculateNewPath()  # Generate a new path to the target
            return

        if self.jammedCounter >= 3:  # Aggressive drivers recalculate paths faster
            self.recalculateNewPath()

        target_coordinates = self.path[0]
        cell_contents = self.model.grid.get_cell_list_contents([target_coordinates])
        traffic_lights = [obj for obj in cell_contents if isinstance(obj, SemaphoreAgent)]
        other_cars = [obj for obj in cell_contents if isinstance(obj, CarAgent) and obj != self]

        # Ignores red lights unless another car is present
        if not traffic_lights or traffic_lights[0].state != "red":
            if not other_cars:
                self.model.grid.move_agent(self, target_coordinates)
                self.pos = target_coordinates
                self.path.pop(0)
                self.jammedCounter = 0
            else:
                self.jammedCounter += 1
        else:
            self.jammedCounter += 1

    def broadcast_intention(self):
        """Aggressive drivers broadcast higher priority."""
        self.model.messages.append({
            "agent_id": self.unique_id,
            "pos": self.pos,
            "intention": "moving" if self.path else "stopping",
            "priority": "high",  # High priority for aggressive drivers
        })
    
    def react_to_messages(self):
        if not self.path:  # Skip if there's no path to react to
            return
        
        for message in self.model.messages:
            if message["agent_id"] == self.unique_id:
                continue
            if "pos" in message and message["pos"] == self.path[0]:
                if message["priority"] == "high":
                    self.jammedCounter += 1  # Stop only for higher-priority agents

class CautiousDriver(CarAgent):
    def move(self):
        if not self.path:
            if self.pos == self.target_pos:  # Ensure the agent is at the target
                self.reached_goal = True
            else:
                print(f"Agent {self.unique_id} is not at the target but has no path.")
                self.recalculateNewPath()  # Generate a new path to the target
            return

        target_coordinates = self.path[0]
        cell_contents = self.model.grid.get_cell_list_contents([target_coordinates])
        traffic_lights = [obj for obj in cell_contents if isinstance(obj, SemaphoreAgent)]
        other_cars = [obj for obj in cell_contents if isinstance(obj, CarAgent) and obj != self]

        # Stops for any potential conflict
        if traffic_lights and traffic_lights[0].state != "green":
            self.jammedCounter += 1
        elif other_cars:
            self.jammedCounter += 1
        else:
            self.model.grid.move_agent(self, target_coordinates)
            self.pos = target_coordinates
            self.path.pop(0)
            self.jammedCounter = 0

    def react_to_messages(self):
        if not self.path:  # Skip if there's no path to react to
            return
        
        for message in self.model.messages:
            if message["agent_id"] == self.unique_id:
                continue
            if "pos" in message and message["pos"] == self.path[0]:
                self.jammedCounter += 1  # Always stop for potential conflicts

class DistractedDriver(CarAgent):
    def move(self):
        if not self.path:
            if self.pos == self.target_pos:  # Ensure the agent is at the target
                self.reached_goal = True
            else:
                print(f"Agent {self.unique_id} is not at the target but has no path.")
                self.recalculateNewPath()  # Generate a new path to the target
            return

        if random.random() < 0.1:  # Introduces random pauses
            self.jammedCounter += 1
            return

        target_coordinates = self.path[0]
        cell_contents = self.model.grid.get_cell_list_contents([target_coordinates])
        traffic_lights = [obj for obj in cell_contents if isinstance(obj, SemaphoreAgent)]
        other_cars = [obj for obj in cell_contents if isinstance(obj, CarAgent) and obj != self]

        if not traffic_lights or traffic_lights[0].state == "green":
            if not other_cars:
                self.model.grid.move_agent(self, target_coordinates)
                self.pos = target_coordinates
                self.path.pop(0)
                self.jammedCounter = 0
            else:
                self.jammedCounter += 1
        else:
            self.jammedCounter += 1

    def react_to_messages(self):
        if random.random() < 0.8:  # 80% chance to react
            super().react_to_messages()

class LearningDriver(CarAgent):
    def __init__(self, unique_id, model, pos, t_pos, path):
        super().__init__(unique_id, model, pos, t_pos, path)
        self.experience = {}  # Stores paths and their success rates

    def recalculateNewPath(self):
        new_target_pos = random.choice(Parkings)
        while new_target_pos == self.target_pos:
            new_target_pos = random.choice(Parkings)
        self.target_pos = new_target_pos
        new_path = astarComplete(self.model.G, self.pos, self.target_pos, manhattan_distance)
        if new_path:
            self.path = new_path
            self.jammedCounter = 0
        else:
            print(f"Agent {self.unique_id} failed to find a path. Retrying...")
            self.recalculateNewPath()

    def move(self):
        if not self.path:
            if self.pos == self.target_pos:  # Ensure the agent is at the target
                self.reached_goal = True
            else:
                print(f"Agent {self.unique_id} is not at the target but has no path.")
                self.recalculateNewPath()  # Generate a new path to the target
            return

        target_coordinates = self.path[0]
        cell_contents = self.model.grid.get_cell_list_contents([target_coordinates])
        traffic_lights = [obj for obj in cell_contents if isinstance(obj, SemaphoreAgent)]
        other_cars = [obj for obj in cell_contents if isinstance(obj, CarAgent) and obj != self]

        if not traffic_lights or traffic_lights[0].state == "green":
            if not other_cars:
                self.model.grid.move_agent(self, target_coordinates)
                self.pos = target_coordinates
                self.path.pop(0)
                self.jammedCounter = 0
            else:
                self.jammedCounter += 1
        else:
            self.jammedCounter += 1

        # Adjust experience after movement
        current_path = tuple(self.path)
        if self.jammedCounter == 0:
            self.experience[current_path] = self.experience.get(current_path, 0) + 1
        else:
            self.experience[current_path] = self.experience.get(current_path, 0) - 1

    def react_to_messages(self):
        if not self.path:  # Skip if there's no path to react to
            return
        
        for message in self.model.messages:
            if message["agent_id"] == self.unique_id:
                continue
            if "pos" in message and message["pos"] == self.path[0]:
                self.experience[tuple(self.path)] = self.experience.get(tuple(self.path), 0) - 1
                self.jammedCounter += 1  # Record negative experience for this path


class ParkingLotAgent(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.pos = pos


class BuildingAgent(Agent):
    def __init__(self, unique_id, model, pos, color):
        super().__init__(unique_id, model)
        self.pos = pos
        self.color = color

    def step(self):
        pass


class SemaphoreAgent(Agent):
    def __init__(self, unique_id, model, pos, state):
        super().__init__(unique_id, model)
        self.pos = pos
        self.state = state # States: "red", "green", "yellow"
        self.timer = 3  # Initial Time

    def change_state(self):
        if self.state == 'red' and self.timer == 0:
            self.state = 'green'
            self.timer = 3  # Green light duration
        elif self.state == 'yellow' and self.timer == 0:
            self.state = 'red'
            self.timer = 2  # Red light duration
        elif self.state == 'green' and self.timer == 0:
            self.state = 'yellow'
            self.timer = 1  # Yellow light duration
        else:
            self.timer -= 1

    def step(self):
        self.change_state()