# Test de normalité sans points extremes 
import pandas as pd
from scipy import stats


donnees = pd.read_csv('jfreechart-test-stats.csv')
donnees.columns = donnees.columns.str.strip()

# Fonction pour éliminer les points extrêmes basée sur l'IQR
def eliminer_points_extremes(df, nom_colonne):
    q1 = df[nom_colonne].quantile(0.25)
    q3 = df[nom_colonne].quantile(0.75)
    iqr = q3 - q1
    limite_basse = q1 - 1.5 * iqr
    limite_haute = q3 + 1.5 * iqr
    return df[(df[nom_colonne] >= limite_basse) & (df[nom_colonne] <= limite_haute)]

# Éliminer les points extrêmes pour TLOC, WMC et TASSERT
donnees_filtrées = eliminer_points_extremes(donnees, 'TLOC')
donnees_filtrées = eliminer_points_extremes(donnees_filtrées, 'WMC')
donnees_filtrées = eliminer_points_extremes(donnees_filtrées, 'TASSERT')

# Effectuer le test de Shapiro-Wilk
for col in ['TLOC', 'WMC', 'TASSERT']:
    stat, p_value = stats.shapiro(donnees_filtrées[col])
    print(f"Test de Shapiro-Wilk pour {col}: Statistique = {stat}, P-value = {p_value}")

    # Interprétation de la p-value
    if p_value > 0.05:
        print(f"La distribution de {col} semble normale (ne rejette pas H0).")
    else:
        print(f"La distribution de {col} ne semble pas normale (rejette H0).")
