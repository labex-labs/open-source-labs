# Durchführen von Grundlegenden Statistiken

Pandas bietet viele Funktionen zur Durchführung von Statistiken. Beispielsweise können Sie den maximalen Wert in einer Spalte mit `max()` finden.

```python
# Finding the maximum age
df["Age"].max()
```

Sie können auch einen schnellen Überblick über die numerischen Daten in einem DataFrame mit `describe()` erhalten.

```python
# Describing the numerical data
df.describe()
```
