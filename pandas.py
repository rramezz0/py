import pandas as pd


data = {
    'Student': ['ramez', 'ramy', 'mohamed', 'sherif', 'ismail']
    'Grade': [80, 78, 60, 50 ,40]
    'Pass/Fail': ['Pass', 'Pass', 'Pass', 'Fail', 'Fail']
}
df = pd.DataFrame(data)

print("Row with index 1:")
print(df.iloc[1])

df_pass = df[df['Pass/Fail'] == 'Pass']

print("\nFiltered DataFrame with 'Pass':")
print(df_pass)
