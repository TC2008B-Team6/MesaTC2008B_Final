import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame based on the data
data = {
    "Driver Type": ["Aggressive", "Cautious", "Distracted", "Learning"],
    "Average Advances": [49.361, 53.6075, 59.356, 50.996],
}

df = pd.DataFrame(data)

# Display the table
plt.figure(figsize=(8, 4))
plt.axis('off')
plt.table(
    cellText=df.values,
    colLabels=df.columns,
    loc='center',
    cellLoc='center',
    colLoc='center',
    cellColours=[['#f0f0f0'] * len(df.columns)] * len(df),  # Optional: Background colors
    colColours=['#d9d9d9'] * len(df.columns)  # Optional: Header background color
)
plt.title("Average Advances by Driver Type", fontsize=14, pad=20)
plt.tight_layout()
plt.savefig("average_advances_table.png", dpi=300)  # Improved resolution for saved image
plt.show()

# Create a bar plot using Seaborn
plt.figure(figsize=(8, 6))
sns.barplot(
    x="Driver Type",
    y="Average Advances",
    data=df,
    palette=["purple", "blue", "pink", "cyan"]
)

# Add titles and labels
plt.title("Average Advances by Driver Type", fontsize=16, pad=15)
plt.xlabel("Driver Type", fontsize=14)
plt.ylabel("Average Advances", fontsize=14)

# Add values on top of bars
for index, row in df.iterrows():
    plt.text(index, row["Average Advances"] + 0.5, f"{row['Average Advances']:.2f}", 
             ha='center', va='bottom', fontsize=12, color='black')

# Show the plot
plt.tight_layout()
plt.savefig("average_advances_barplot.png", dpi=300)  # Save the bar plot
plt.show()
