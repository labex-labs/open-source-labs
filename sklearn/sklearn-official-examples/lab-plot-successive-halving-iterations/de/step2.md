# Laden des Datensatzes

Die Funktion `make_classification` aus dem Modul `sklearn.datasets` wird verwendet, um einen Klassifizierungsdatensatz zu generieren. Der Datensatz enthält 400 Proben mit 12 Merkmalen. Der Code zum Laden des Datensatzes lautet wie folgt:

```python
rng = np.random.RandomState(0)
X, y = datasets.make_classification(n_samples=400, n_features=12, random_state=rng)
```
