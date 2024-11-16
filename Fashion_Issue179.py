import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Trend': [
        'Y2K Fashion', 'Athleisure', 'Sustainable Clothing',
        'Gender-Neutral Fashion', 'Vintage Thrifting', 'DIY Customization'
    ],
    'Popularity_Score': [85, 90, 75, 80, 70, 65]
}

df = pd.DataFrame(data)

sns.set_style("whitegrid")

plt.figure(figsize=(10, 6))
barplot = sns.barplot(
    x='Popularity_Score', y='Trend', data=df, palette='viridis', orient='h'
)
barplot.set_title('Popularity of Gen Z Fashion Trends in 2024', fontsize=16)
barplot.set_xlabel('Popularity Score', fontsize=14)
barplot.set_ylabel('Fashion Trend', fontsize=14)

plt.tight_layout()
plt.show()
