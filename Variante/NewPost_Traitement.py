import csv
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict


def mapper(path_csv):
    results = []
    with open(path_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for line in reader:
            if len(line) != 5:
                continue
            sexe, prenom, annais, dept, nombre = line
            if not (annais and sexe and nombre and dept):
                continue
            if '_' in prenom:
                continue
            try:
                annee = int(annais)
                decennie = (annee // 10) * 10
                key = (prenom.upper(), decennie)
                results.append((key, int(nombre)))
            except:
                continue
    return results


def reducer(mapped_data):
    aggregated = defaultdict(int)
    for key, value in mapped_data:
        aggregated[key] += value
    return aggregated  


def plot(data_dict, top_n=5):
    # Convertir en DataFrame
    df = pd.DataFrame([(*k, v) for k, v in data_dict.items()], columns=["prenom", "decennie", "total"])
    df["decennie"] = df["decennie"].astype(int)

    # Extraire les décennies triées
    decades = sorted(df["decennie"].unique())

    for dec in decades:
        top_dec = df[df["decennie"] == dec].sort_values("total", ascending=False).head(top_n)

        # Tracer le graphique en barres
        plt.figure(figsize=(8, 5))
        plt.bar(top_dec["prenom"], top_dec["total"], color='skyblue')
        plt.title(f"Top {top_n} prénoms dans les années {dec}s")
        plt.xlabel("Prénom")
        plt.ylabel("Nombre de naissances")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()


if __name__ == "__main__":
    csv_path = "dpt2022_valid.csv"
    mapped = mapper(csv_path)
    reduced = reducer(mapped)
    plot(reduced, top_n=5)
