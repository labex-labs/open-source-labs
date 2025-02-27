# データの前処理

SGD を適用する前に、データを前処理することが多くの場合有益です。この場合、scikit-learn の `StandardScaler` を使用して特徴量を標準化します。

```python
scaler = StandardScaler()
X = scaler.fit_transform(X)
```
