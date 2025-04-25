# ランダム化 SVD を使った主特異値ベクトルの計算

scikit-learn で実装された randomized_svd メソッドを使って主特異値ベクトルを計算します。

```python
from sklearn.decomposition import randomized_svd

print("randomized_svd を使って主特異値ベクトルを計算中")
U, s, V = randomized_svd(X, 5, n_iter=3)
```
