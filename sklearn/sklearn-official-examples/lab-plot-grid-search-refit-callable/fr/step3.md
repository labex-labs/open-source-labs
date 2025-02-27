# Charger les données et définir le pipeline

Nous allons charger le jeu de données digits de scikit-learn et définir un pipeline composé de PCA et de LinearSVC.

```python
pipe = Pipeline(
    [
        ("reduce_dim", PCA(random_state=42)),
        ("classify", LinearSVC(random_state=42, C=0.01, dual="auto")),
    ]
)

X, y = load_digits(return_X_y=True)
```
