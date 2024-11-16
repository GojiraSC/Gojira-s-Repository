import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': [2018, 2019, 2020, 2021, 2022, 2023],
    'Climate_Change': [50, 60, 70, 80, 90, 100],
    'Pollution_Control': [40, 45, 50, 55, 60, 70],
    'Carbon_Emissions': [30, 35, 40, 45, 50, 65],
    'Public_Health': [20, 25, 30, 35, 40, 50]
}

df = pd.DataFrame(data)

df.set_index('Year', inplace=True)

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Climate_Change'], marker='o', label='Climate Change')
plt.plot(df.index, df['Pollution_Control'], marker='o', label='Pollution Control')
plt.plot(df.index, df['Carbon_Emissions'], marker='o', label='Carbon Emissions')
plt.plot(df.index, df['Public_Health'], marker='o', label='Public Health')
plt.title("Trends in Environmental Policy Topics Over Time")
plt.xlabel("Year")
plt.ylabel("Frequency of Mentions")
plt.legend()
plt.grid(True)
plt.show()

latest_year = df.index[-1]
df_latest = df.loc[latest_year]

plt.figure(figsize=(10, 6))
df_latest.plot(kind='bar', color='skyblue')
plt.title(f"Environmental Policy Topics Frequency in {latest_year}")
plt.xlabel("Topic")
plt.ylabel("Frequency of Mentions")
plt.xticks(rotation=45)
plt.show()
