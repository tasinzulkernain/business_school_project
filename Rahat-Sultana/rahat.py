import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('academic_expenditure_01_22.csv')

# Extract Computing department data
Bioengineering_data = data[data['department_name'] == 'Computing']
years = [col for col in Bioengineering_data.columns if col != 'department_name']
values = Bioengineering_data.iloc[0, 1:].tolist()

# Convert year strings to just the starting year (e.g., "2001-2002" → 2001)
year_labels = [int(year.split('-')[0]) for year in years]

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(year_labels, values, marker='o', color='blue', linewidth=2)
plt.title('Computing Department Student Pass Rates (2001-2021)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(year_labels, rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('computing_students.png')
print("Graph saved as computing_students.png")