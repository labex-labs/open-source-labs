# Inverse Transform

In this step, we will perform an inverse transform on the reduced dataset to restore the original number of features.

```python
X_restored = agglo.inverse_transform(X_reduced)
images_restored = np.reshape(X_restored, images.shape)
```
