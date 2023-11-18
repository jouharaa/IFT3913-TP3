import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats

donnees = pd.read_csv('jfreechart-test-stats.csv')

donnees.columns = donnees.columns.str.strip()

# Ajout de droites de régression linéaire
plt.figure(figsize=(10, 6))
sns.regplot(x='TLOC', y='TASSERT', data=donnees)
plt.title('Régression linéaire entre TLOC et TASSERT')
plt.show()

plt.figure(figsize=(10, 6))
sns.regplot(x='WMC', y='TASSERT', data=donnees)
plt.title('Régression linéaire entre WMC et TASSERT')
plt.show()

# Calcul de la droite de régression pour TLOC et TASSERT
slope_tloc, intercept_tloc, r_value_tloc, p_value_tloc, std_err_tloc = stats.linregress(donnees['TLOC'], donnees['TASSERT'])
print(f"Droite de régression pour TLOC et TASSERT : y = {slope_tloc:.2f}x + {intercept_tloc:.2f}")

# Calcul de la droite de régression pour WMC et TASSERT
slope_wmc, intercept_wmc, r_value_wmc, p_value_wmc, std_err_wmc = stats.linregress(donnees['WMC'], donnees['TASSERT'])
print(f"Droite de régression pour WMC et TASSERT : y = {slope_wmc:.2f}x + {intercept_wmc:.2f}")

# Calcul des coefficients de corrélation Spearman
corr_tloc_tassert_spearman = donnees['TLOC'].corr(donnees['TASSERT'], method='spearman')
corr_wmc_tassert_spearman = donnees['WMC'].corr(donnees['TASSERT'], method='spearman')


# la distribution n'est pas normale d'apres la tache 1, alors la methode utilisee est spearman
print(f"Correlation spearman entre TLOC et TASSERT : {corr_tloc_tassert_spearman}")
print(f"Correlation spearman entre WMC et TASSERT : {corr_wmc_tassert_spearman}")

