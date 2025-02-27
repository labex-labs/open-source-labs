# 逆変換

このステップでは、縮小されたデータセットに対して逆変換を行い、元の特徴数を復元します。

```python
X_restored = agglo.inverse_transform(X_reduced)
images_restored = np.reshape(X_restored, images.shape)
```
