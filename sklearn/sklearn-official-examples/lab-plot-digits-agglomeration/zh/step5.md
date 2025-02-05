# 逆变换

在这一步中，我们将对降维后的数据集执行逆变换，以恢复原始的特征数量。

```python
X_restored = agglo.inverse_transform(X_reduced)
images_restored = np.reshape(X_restored, images.shape)
```
