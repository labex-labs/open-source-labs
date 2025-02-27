# Ajuster le modèle de mélange gaussien

Nous allons maintenant ajuster un GMM à l'ensemble de données en utilisant la classe GaussianMixture de scikit-learn. Nous allons définir le nombre de composantes sur 2 et le type de covariance sur "full".

```python
# ajuster un modèle de mélange gaussien avec deux composantes
clf = mixture.GaussianMixture(n_components=2, covariance_type="full")
clf.fit(X_train)
```
