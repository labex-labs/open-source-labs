# Обратное преобразование

В этом шаге мы выполним обратное преобразование для уменьшенного набора данных, чтобы восстановить исходное количество признаков.

```python
X_restored = agglo.inverse_transform(X_reduced)
images_restored = np.reshape(X_restored, images.shape)
```
