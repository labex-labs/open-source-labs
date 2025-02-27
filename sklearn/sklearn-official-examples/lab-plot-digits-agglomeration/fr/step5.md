# Transformée inverse

Dans cette étape, nous allons effectuer une transformée inverse sur l'ensemble de données réduit pour restaurer le nombre original de fonctionnalités.

```python
X_restored = agglo.inverse_transform(X_reduced)
images_restored = np.reshape(X_restored, images.shape)
```
