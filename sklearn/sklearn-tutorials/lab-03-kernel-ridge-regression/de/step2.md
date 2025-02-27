# Synthetische Daten generieren

Als nächstes generieren wir einige synthetische Daten, mit denen wir arbeiten können. Wir werden eine sinusförmige Zielfunktion erstellen und ihr einige zufälliges Rauschen hinzufügen.

```python
# Generate input data
np.random.seed(0)
X = np.sort(5 * np.random.rand(100, 1), axis=0)
y = np.sin(X).ravel()
y += 0.5 * (0.5 - np.random.rand(y.size))
```
