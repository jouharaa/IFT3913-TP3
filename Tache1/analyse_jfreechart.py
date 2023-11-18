import pandas as pd
import matplotlib.pyplot as plt

donnees = pd.read_csv('jfreechart-test-stats.csv')

donnees.columns = donnees.columns.str.strip()

data_to_plot = [donnees['TLOC'], donnees['WMC'], donnees['TASSERT']]

plt.figure(figsize=(10, 6)) 

# Création du graphique de boîtes à moustaches
plt.boxplot(data_to_plot)

plt.title('Boîtes à moustaches pour TLOC, WMC et TASSERT')
plt.xticks([1, 2, 3], ['TLOC', 'WMC', 'TASSERT'])
plt.ylabel('Valeurs')

# Afficher graphique
plt.show()
