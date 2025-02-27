# ランダム化SVDを使った主特異値ベクトルの計算

scikit-learnで実装されたrandomized_svdメソッドを使って主特異値ベクトルを計算します。

```python
from sklearn.decomposition import randomized_svd

print("randomized_svdを使って主特異値ベクトルを計算中")
U, s, V = randomized_svd(X, 5, n_iter=3)
```
