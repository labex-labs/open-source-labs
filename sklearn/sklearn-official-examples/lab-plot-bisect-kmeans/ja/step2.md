# サンプルデータの生成

このステップでは、scikit-learn の `make_blobs()` 関数を使ってサンプルデータを生成します。2つの中心を持つ 10000 個のサンプルを生成します。

```python
n_samples = 10000
random_state = 0
X, _ = make_blobs(n_samples=n_samples, centers=2, random_state=random_state)
```
