# Charger et préparer l'ensemble de données

Nous chargons l'ensemble de données des chiffres et le préparons pour le regroupement en extrayant les données et les étiquettes cibles. Nous définissons également la graine aléatoire sur zéro pour garantir la reproductibilité.

```python
digits = datasets.load_digits()
X, y = digits.data, digits.target
n_samples, n_features = X.shape
np.random.seed(0)
```
