# Ajustez un modèle mixte gaussien

Maintenant, nous pouvons ajuster un modèle mixte gaussien à nos données en utilisant la classe `GaussianMixture` du module `sklearn.mixture`. Spécifiez le nombre de composants souhaité et tout autre paramètre que vous voulez utiliser.

```python
# Ajustez un modèle mixte gaussien
gmm = GaussianMixture(n_components=3)
gmm.fit(X_train)
```
