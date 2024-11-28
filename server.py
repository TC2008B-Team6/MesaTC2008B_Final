from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from agent import CarAgent, ParkingLotAgent, BuildingAgent, SemaphoreAgent, AggressiveDriver, CautiousDriver, DistractedDriver, LearningDriver
from model import TrafficModel
from map import grid_size

def color_agent(agent):
    color = {}
    if isinstance(agent, AggressiveDriver):
        color = {
            "Shape": "circle",
            "r": 0.5,
            "Color": "purple",  # Aggressive drivers are red
            "Filled": "true",
            "Layer": 3,
        }
    elif isinstance(agent, CautiousDriver):
        color = {
            "Shape": "circle",
            "r": 0.5,
            "Color": "blue",  # Cautious drivers are blue
            "Filled": "true",
            "Layer": 3,
        }
    elif isinstance(agent, DistractedDriver):
        color = {
            "Shape": "circle",
            "r": 0.5,
            "Color": "pink",  # Distracted drivers are yellow
            "Filled": "true",
            "Layer": 3,
        }
    elif isinstance(agent, LearningDriver):
        color = {
            "Shape": "circle",
            "r": 0.5,
            "Color": "cyan",  # Learning drivers are green
            "Filled": "true",
            "Layer": 3,
        }
    elif isinstance(agent, CarAgent):
        color = {
                "Shape": "circle",
                "r": 0.5,
                "Color": "black",
                "Filled": "true",
                "Layer": 3,
                }
    elif isinstance(agent, ParkingLotAgent):
        color = {
                "Shape": "rect",
                "Color": "gray",
                "Filled": "true",
                "Layer": 0,
                "w": 1,
                "h": 1
                }
    elif isinstance(agent, SemaphoreAgent):
        if agent.state == 'red':
            color = {
                    "Shape": "rect",
                    "Color": "red",
                    "Filled": "true",
                    "Layer": 0,
                    "w": 0.7,
                    "h": 0.7
                    }
        elif agent.state == 'yellow':
            color = {
                    "Shape": "rect",
                    "Color": "yellow",
                    "Filled": "true",
                    "Layer": 0,
                    "w": 0.7,
                    "h": 0.7
                    }
        else:
            color = {
                    "Shape": "rect",
                    "Color": "green",
                    "Filled": "true",
                    "Layer": 0,
                    "w": 0.7,
                    "h": 0.7
                    }
    elif isinstance(agent, BuildingAgent):
        color = {
                "Shape": "rect",
                "Color": agent.color,
                "Filled": "true",
                "Layer": 0,
                "w": 1,
                "h": 1
                }
    return color


grid = CanvasGrid(color_agent,grid_size, grid_size)

advance_chart = ChartModule(
    [
        {"Label": "Aggressive Advances", "Color": "Purple"},
        {"Label": "Cautious Advances", "Color": "Blue"},
        {"Label": "Distracted Advances", "Color": "Pink"},
        {"Label": "Learning Advances", "Color": "Cyan"}
    ],
    data_collector_name='datacollector'  # Must match the data collector in the model
)


server = ModularServer(
    TrafficModel, [grid, advance_chart], "Traffic Model", {"width": grid_size, "height": grid_size, "n_cars": 15}
)


server.port = 8521

server.launch()