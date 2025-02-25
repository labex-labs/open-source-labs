# Generieren der Daten

Als nächstes werden wir einige Beispiel-Daten generieren, die wir in unseren Boxplots verwenden werden. Für diesen Tutorial werden wir die folgenden Daten verwenden:

```python
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
```
