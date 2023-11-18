import pandas as pd
from scipy import stats

donnees = pd.read_csv('jfreechart-test-stats.csv')

donnees.columns = donnees.columns.str.strip()

# Test de Shapiro-Wilk
for col in ['TLOC', 'WMC', 'TASSERT']:
    stat, p_value = stats.shapiro(donnees[col])
    print(f"Test de Shapiro-Wilk pour {col}:")
    print(f"  Statistique de test : {stat}")
    print(f"  P-value : {p_value}")

    # Interprétation
    alpha = 0.05
    if p_value > alpha:
        print(f"  La distribution de {col} semble normale (ne rejette pas H0)\n")
    else:
        print(f"  La distribution de {col} ne semble pas normale (rejette H0)\n")
