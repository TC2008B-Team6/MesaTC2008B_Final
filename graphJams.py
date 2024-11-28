import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data based on the uploaded table
data = {
    "Drivers": ["10 drivers", "20 drivers", "30 drivers", "40 drivers", "50 drivers", "Average"],
    "Aggressive": [44.6, 143.6, 267.8, 413.4, 473.6, 268.6],
    "Cautious": [52.6, 150.4, 252.2, 341.2, 477.2, 254.72],
    "Distracted": [44.2, 119.4, 219.8, 304.4, 442.4, 226.04],
    "Learning": [32.8, 119.8, 238.8, 348.4, 474.8, 242.92],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the table
plt.figure(figsize=(8, 4))
plt.axis('off')
plt.table(
    cellText=df.values,
    colLabels=df.columns,
    loc='center',
    cellLoc='center'
)
plt.title("Jammed Encounters by Driver Type and Number of Cars", fontsize=14)
plt.tight_layout()
plt.savefig("jammed_encounters_table.png")  # Save the table as an image (optional)
plt.show()

# Visualization: Line plot with specific colors
plt.figure(figsize=(10, 6))

# Define the custom colors
colors = {
    "Aggressive": "purple",
    "Cautious": "blue",
    "Distracted": "pink",
    "Learning": "cyan"
}

# Plot each line with the specified color
for col in ["Aggressive", "Cautious", "Distracted", "Learning"]:
    if col != "Average":  # Exclude average from line plot
        sns.lineplot(data=df[:-1], x="Drivers", y=col, label=col, color=colors[col])

# Add titles and labels
plt.title("Jammed Encounters Trends by Driver Type", fontsize=16)
plt.xlabel("Number of Drivers", fontsize=14)
plt.ylabel("Jammed Encounters", fontsize=14)
plt.legend(title="Driver Type", fontsize=12)
plt.xticks(rotation=45, fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()
