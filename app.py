from flask import Flask, request
import json
from model import TrafficModel
from map import grid_size

app = Flask(__name__)

model = TrafficModel(grid_size, grid_size, 30)

def carToJSON(lists):
    cars_list = [
        {
            "id": car_data[0], 
            "x1": car_data[1],
            "z1": car_data[2],
            "x2": car_data[3],
            "z2": car_data[4],
            "x3": car_data[5],
            "z3": car_data[6],
        }
        for car_data in lists
    ]
    return {"Items": cars_list}

def semaphoreToJSON(lists):
    sem_list = [
        {
            "id": json.dumps(sem_data[0]),
            "position": json.dumps(sem_data[1]),
            "state": sem_data[2]
        }
        for sem_data in lists]
    result_dict = {"Items": sem_list}
    return result_dict

@app.route('/getSemaphoreState', methods=['GET'])
def getSemaphoreState():
    if request.method == 'GET':
        state = model.getSemaphoreState()
        model.step()
        return semaphoreToJSON(state)

@app.route('/getCarPosition', methods=['GET'])
def getCarPositions():
    if request.method == 'GET':
        state = model.getCarState()
        # Log car state for debugging
        print(f"Car state before step: {state}")
        model.step()  # Advance the model state
        return carToJSON(state)


if __name__ == '__main__':
 
    app.run(debug=True, port=8000)