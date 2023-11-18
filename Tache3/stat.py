import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

donnees = pd.read_csv('jfreechart-test-stats.csv')
donnees.columns = donnees.columns.str.strip()

group_plus_20_assertions = donnees[donnees['TASSERT'] > 20]
group_moins_20_assertions = donnees[donnees['TASSERT'] <= 20]

# Test de Mann-Whitney pour TLOC
tloc_stat, tloc_p = stats.mannwhitneyu(group_plus_20_assertions['TLOC'], group_moins_20_assertions['TLOC'])

# Test de Mann-Whitney pour WMC
wmc_stat, wmc_p = stats.mannwhitneyu(group_plus_20_assertions['WMC'], group_moins_20_assertions['WMC'])

print(f"Résultats du test de Mann-Whitney pour TLOC: U = {tloc_stat}, p-value = {tloc_p}")
print(f"Résultats du test de Mann-Whitney pour WMC: U = {wmc_stat}, p-value = {wmc_p}")
