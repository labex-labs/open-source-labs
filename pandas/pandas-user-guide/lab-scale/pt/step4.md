# Usar Chunking (Fragmentação)

Chunking (fragmentação) é um método para dividir um problema grande em problemas menores que podem ser resolvidos independentemente. Contanto que cada chunk (fragmento) caiba na memória, você pode trabalhar com conjuntos de dados que são muito maiores do que a memória.

```python
files = pathlib.Path("data/timeseries/").glob("ts*.parquet")
counts = pd.Series(dtype=int)
for path in files:
    df = pd.read_parquet(path)
    counts = counts.add(df["name"].value_counts(), fill_value=0)
counts.astype(int)
```
