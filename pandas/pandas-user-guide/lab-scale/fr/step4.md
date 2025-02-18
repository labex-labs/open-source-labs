# Utiliser le fractionnement (chunking)

Le fractionnement (chunking) est une méthode consistant à diviser un grand problème en petits problèmes qui peuvent être résolus indépendamment. Tant que chaque fraction (chunk) rentre en mémoire, vous pouvez travailler avec des ensembles de données beaucoup plus volumineux que la mémoire disponible.

```python
files = pathlib.Path("data/timeseries/").glob("ts*.parquet")
counts = pd.Series(dtype=int)
for path in files:
    df = pd.read_parquet(path)
    counts = counts.add(df["name"].value_counts(), fill_value=0)
counts.astype(int)
```
