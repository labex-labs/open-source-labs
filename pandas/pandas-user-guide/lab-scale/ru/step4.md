# Использование разбиения на части (chunking)

Разбиение на части (chunking) - это метод, который позволяет разбить большую задачу на меньшие задачи, которые можно решать независимо. Пока каждая часть помещается в память, вы можете работать с наборами данных, которые намного больше объема памяти.

```python
files = pathlib.Path("data/timeseries/").glob("ts*.parquet")
counts = pd.Series(dtype=int)
for path in files:
    df = pd.read_parquet(path)
    counts = counts.add(df["name"].value_counts(), fill_value=0)
counts.astype(int)
```
