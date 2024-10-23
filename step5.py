import matplotlib.pyplot as plt
import pandas as pd
import glob

csv_files = glob.glob('*.csv')

dataframes = []
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

data = pd.concat(dataframes, ignore_index=True)

category_counts = data['catégorie'].value_counts()
plt.figure(figsize=(10, 6))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Répartition des livres par catégorie')
plt.axis('equal')
plt.show()

average_prices = data.groupby('catégorie')['prix_avec_taxe'].mean().sort_values()
plt.figure(figsize=(12, 8))
average_prices.plot(kind='barh', color='skyblue')
plt.title('Prix moyen des livres par catégorie')
plt.xlabel('Prix moyen (incluant les taxes)')
plt.ylabel('Catégorie')
plt.grid(True)
plt.show()