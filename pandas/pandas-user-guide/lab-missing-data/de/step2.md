# Fehlende Werte erkennen

Als nächstes verwenden wir die Funktionen `isna` und `notna`, um fehlende Werte zu erkennen.

```python
# Verwenden Sie isna und notna, um fehlende Werte zu erkennen
pd.isna(df2["one"])
df2["four"].notna()
df2.isna()
```
