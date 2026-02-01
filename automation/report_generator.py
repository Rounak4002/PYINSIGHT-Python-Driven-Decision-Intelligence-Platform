import pandas as pd

df = pd.read_csv('../data/cleaned_data.csv')

summary = df.groupby('region')['revenue'].sum().reset_index()

summary.to_excel('weekly_report.xlsx', index=False)

print("Report generated successfully.")
