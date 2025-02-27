# Discrétiser la caractéristique d'entrée

Dans cette étape, nous allons utiliser la classe KBinsDiscretizer pour discrétiser la caractéristique d'entrée. Nous allons créer 10 classes et utiliser le codage one-hot pour transformer les données.

```python
enc = KBinsDiscretizer(n_bins=10, encode="onehot")
X_binned = enc.fit_transform(X)
```
