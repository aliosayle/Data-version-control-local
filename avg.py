import pandas as pd

df = pd.read_csv('earthquake_data.csv')

average_strength = df['Strength'].mean()
print(f'Average Earthquake Strength: {average_strength}')
