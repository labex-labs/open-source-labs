# Zufällige Daten generieren

Als nächstes werden wir zwei Arrays mit zufälligen Daten mit NumPy generieren. Wir werden diese Arrays verwenden, um Kreuzkorrelation und Autokorrelation zu demonstrieren.

```python
np.random.seed(19680801)
x, y = np.random.randn(2, 100)
```
