# Charger l'ensemble de données MNIST

Nous allons charger l'ensemble de données MNIST en utilisant la fonction `fetch_openml` de scikit-learn. Nous sélectionnerons également un sous-ensemble des données en définissant le nombre d'`échantillons d'entraînement` sur 5000.

```python
# Diminuer pour une convergence plus rapide
t0 = time.time()
train_samples = 5000

# Charger les données à partir de https://www.openml.org/d/554
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
