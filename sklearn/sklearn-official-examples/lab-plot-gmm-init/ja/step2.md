# 初期平均値を取得する関数を定義する

次に、サンプルデータ、初期化方法、および乱数シードを入力として受け取り、初期化平均値を返す関数 `get_initial_means` を定義します。

```python
def get_initial_means(X, init_params, r):
    # Run a GaussianMixture with max_iter=0 to output the initialization means
    gmm = GaussianMixture(
        n_components=4, init_params=init_params, tol=1e-9, max_iter=0, random_state=r
    ).fit(X)
    return gmm.means_
```
