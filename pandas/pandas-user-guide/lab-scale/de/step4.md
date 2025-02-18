# Chunking (Teilen von Daten) verwenden

Chunking ist eine Methode, um ein großes Problem in kleinere Probleme aufzuteilen, die unabhängig voneinander gelöst werden können. Solange jeder Datenblock (Chunk) in den Speicher passt, können Sie mit Datensätzen arbeiten, die viel größer sind als der verfügbare Speicher.

```python
files = pathlib.Path("data/timeseries/").glob("ts*.parquet")
counts = pd.Series(dtype=int)
for path in files:
    df = pd.read_parquet(path)
    counts = counts.add(df["name"].value_counts(), fill_value=0)
counts.astype(int)
```
