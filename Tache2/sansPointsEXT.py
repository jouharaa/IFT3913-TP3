import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats

donnees = pd.read_csv('jfreechart-test-stats.csv')
donnees.columns = donnees.columns.str.strip()

def eliminer_points_extremes(df, nom_colonne):
    q1 = df[nom_colonne].quantile(0.25)
    q3 = df[nom_colonne].quantile(0.75)
    iqr = q3 - q1
    limite_basse = q1 - 1.5 * iqr
    limite_haute = q3 + 1.5 * iqr
    filtre = df[nom_colonne].between(limite_basse, limite_haute, inclusive='both')
    return df[filtre]

donnees = eliminer_points_extremes(donnees, 'TLOC')
donnees = eliminer_points_extremes(donnees, 'WMC')
donnees = eliminer_points_extremes(donnees, 'TASSERT')

plt.figure(figsize=(10, 6))
sns.regplot(x='TLOC', y='TASSERT', data=donnees)
plt.title('Régression linéaire entre TLOC et TASSERT')
plt.xlabel('TLOC (Total Lines of Code)')
plt.ylabel('TASSERT (Total Assertions)')
plt.show()

plt.figure(figsize=(10, 6))
sns.regplot(x='WMC', y='TASSERT', data=donnees)
plt.title('Régression linéaire entre WMC et TASSERT')
plt.xlabel('WMC (Weighted Methods per Class)')
plt.ylabel('TASSERT (Total Assertions)')
plt.show()

for pair in [('TLOC', 'TASSERT'), ('WMC', 'TASSERT')]:
    slope, intercept, r_value, p_value, std_err = stats.linregress(donnees[pair[0]], donnees[pair[1]])
    corr_spearman = donnees[pair[0]].corr(donnees[pair[1]], method='spearman')
    print(f"Droite de regression pour {pair[0]} et {pair[1]} : y = {slope:.2f}x + {intercept:.2f}")
    # la distribution n'est pas normale d'apres la tache 1, alors la methode utilisee est spearman
    print(f"Correlation Spearman entre {pair[0]} et {pair[1]} : {corr_spearman}\n")
