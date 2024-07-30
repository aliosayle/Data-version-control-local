import pandas as pd

# Create a DataFrame of earthquake strength
data = {'Location': ['Location1', 'Location2', 'Location3'],
        'Strength': [5.2, 6.3, 5.8]}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_path = 'earthquake_data.csv'
df.to_csv(csv_path, index=False)
