from model import TrafficModel
from mesa.batchrunner import BatchRunner
import pandas as pd

# Define parameters for batch runs
fixed_params = {
    "width": 24,
    "height": 24
}

variable_params = {
    "n_cars": [30],  # Example varying the number of cars
}

# Initialize the BatchRunner
batch_runner = BatchRunner(
    TrafficModel,
    variable_params,
    fixed_params,
    iterations=20,  # Number of runs per parameter combination
    max_steps=100,  # Maximum number of steps for each simulation
    model_reporters={"DataCollector": lambda model: model.datacollector}
)

# Run batch simulations
batch_runner.run_all()

# Collect results
batch_data = batch_runner.get_model_vars_dataframe()

# Process DataCollector objects
all_data = []
for index, row in batch_data.iterrows():
    data_collector = row["DataCollector"]
    if data_collector is not None:
        # Get data from the DataCollector
        data = data_collector.get_model_vars_dataframe()
        data["Run"] = index
        all_data.append(data)

# Combine all data into a single DataFrame
if all_data:
    full_data = pd.concat(all_data)
    # Save to CSV
    full_data.to_csv("simulation_results.csv")
    print("Simulation results saved to simulation_results.csv")
else:
    print("No data collected during simulations.")
