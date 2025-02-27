# Berechne die Koeffizienten eines Bayesian Ridge mit GridSearch

```python
cv = KFold(2)  # Kreuzvalidierungsgenerator zur Modellauswahl
ridge = BayesianRidge()
cachedir = tempfile.mkdtemp()
mem = Memory(location=cachedir, verbose=1)
```
