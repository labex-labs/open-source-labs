# Daten generieren

Wir werden einige Beispiel-Daten generieren, auf die wir unsere Strafen anwenden können. Für dieses Beispiel werden wir zwei Klassen von Daten mit jeweils 100 Proben generieren.

```python
np.random.seed(42)

# Generate two classes of data
X = np.random.randn(200, 2)
y = np.repeat([1, -1], 100)
```
