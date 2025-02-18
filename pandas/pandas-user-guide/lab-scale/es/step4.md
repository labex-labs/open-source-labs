# Utilizar División en Fragmentos (Chunking)

La división en fragmentos (chunking) es un método para dividir un problema grande en problemas más pequeños que se pueden resolver de forma independiente. Siempre y cuando cada fragmento quepa en memoria, se pueden trabajar con conjuntos de datos mucho más grandes que la memoria disponible.

```python
files = pathlib.Path("data/timeseries/").glob("ts*.parquet")
counts = pd.Series(dtype=int)
for path in files:
    df = pd.read_parquet(path)
    counts = counts.add(df["name"].value_counts(), fill_value=0)
counts.astype(int)
```
