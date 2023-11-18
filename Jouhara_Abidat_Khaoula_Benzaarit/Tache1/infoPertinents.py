import pandas as pd

donnees = pd.read_csv('jfreechart-test-stats.csv')

donnees.columns = donnees.columns.str.strip()

for col in ['TLOC', 'WMC', 'TASSERT']:
    print(f"Statistiques pour {col}:")

    q1 = donnees[col].quantile(0.25)  # Quartile inférieur
    q3 = donnees[col].quantile(0.75)  # Quartile supérieur
    mediane = donnees[col].median()    # Médiane

    iqr = q3 - q1

    # Calcul des limites 
    limite_inferieure = max(q1 - 1.5 * iqr, 0)
    limite_superieure = min(q3 + 1.5 * iqr, donnees[col].max()) 


    print(f"  Quartile inferieur (Q1) : {q1}")
    print(f"  Mediane : {mediane}")
    print(f"  Quartile superieur (Q3) : {q3}")
    print(f"  Limite inferieure : {limite_inferieure}")
    print(f"  Limite superieure : {limite_superieure}\n")
