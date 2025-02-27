# Jeu de données transformé

Nous utiliserons les caractéristiques combinées pour transformer le jeu de données.

```python
X_features = combined_features.fit(X, y).transform(X)
print("Combined space has", X_features.shape[1], "features")
```
