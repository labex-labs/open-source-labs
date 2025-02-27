# Erzeugen eines Toy-Datensatzes

Wir werden nun einen Toy-Datensatz mit der Funktion make_regression aus scikit-learn erzeugen. Wir werden einen Datensatz mit 20 Proben, einem Merkmal und einem Zufallszahlengenerator mit dem Seed 0 erzeugen. Wir werden auch etwas Rauschen zum Datensatz hinzufügen.

```python
rng = np.random.RandomState(0)
X, y = make_regression(
    n_samples=20, n_features=1, random_state=0, noise=4.0, bias=100.0
)
```
