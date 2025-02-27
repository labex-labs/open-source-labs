# Inverse Transformation

In diesem Schritt werden wir eine inverse Transformation auf dem reduzierten Dataset durchführen, um die ursprüngliche Anzahl der Merkmale wiederherzustellen.

```python
X_restored = agglo.inverse_transform(X_reduced)
images_restored = np.reshape(X_restored, images.shape)
```
