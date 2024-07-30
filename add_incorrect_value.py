import pandas as pd

# Load the existing earthquake data
csv_path = 'earthquake_data.csv'
df = pd.read_csv(csv_path)

# Add an incorrect value
incorrect_value = pd.DataFrame([{'Location': 'Location4', 'Strength': 100.0}])

# Use concat to add the incorrect value
df = pd.concat([df, incorrect_value], ignore_index=True)

# Save the modified DataFrame back to the CSV file
df.to_csv(csv_path, index=False)
