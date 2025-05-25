# Transformação Inversa

Neste passo, realizaremos uma transformação inversa no conjunto de dados reduzido para restaurar o número original de recursos.

```python
X_restored = agglo.inverse_transform(X_reduced)
images_restored = np.reshape(X_restored, images.shape)
```
