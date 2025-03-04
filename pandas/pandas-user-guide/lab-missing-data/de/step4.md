# Berechnungen mit fehlenden Daten durchführen

Wir werden einige grundlegende arithmetische und statistische Berechnungen mit fehlenden Daten durchführen.

```python
# Berechnungen mit fehlenden Daten durchführen
df["one"].sum()
df.mean(axis=1, numeric_only=True)
df.cumsum()
```
