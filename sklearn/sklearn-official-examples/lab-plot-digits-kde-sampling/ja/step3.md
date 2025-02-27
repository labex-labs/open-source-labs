# 新しいサンプルの生成

データから 44 個の新しい点をサンプリングするために、最適な推定器を使用します。その後、PCA の逆変換を使用して、新しいデータを元の 64 次元に戻します。

```python
# sample 44 new points from the data
new_data = kde.sample(44, random_state=0)
new_data = pca.inverse_transform(new_data)
```
