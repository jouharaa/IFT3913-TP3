import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

donnees = pd.read_csv('jfreechart-test-stats.csv')
donnees.columns = donnees.columns.str.strip()

group_plus_20_assertions = donnees[donnees['TASSERT'] > 20]
group_moins_20_assertions = donnees[donnees['TASSERT'] <= 20]

# Vérification de la normalité pour TLOC et WMC dans chaque groupe
for col in ['TLOC', 'WMC']:
    print(f"Test de Shapiro-Wilk pour {col} dans le groupe avec plus de 20 assertions:")
    print(stats.shapiro(group_plus_20_assertions[col]))
    print(f"Test de Shapiro-Wilk pour {col} dans le groupe avec moins de 20 assertions:")
    print(stats.shapiro(group_moins_20_assertions[col]))

