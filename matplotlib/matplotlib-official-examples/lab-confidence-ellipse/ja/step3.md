# `get_correlated_dataset` 関数を定義する

また、指定された平均、次元、および相関を持つ 2 次元データセットを生成する関数が必要です。

```python
def get_correlated_dataset(n, dependency, mu, scale):
    """
    指定された 2 次元の平均 (mu) と次元 (scale) を持つランダムな 2 次元データセットを作成します。
    相関はパラメータ 'dependency'（2x2 行列）で制御できます。
    """
    latent = np.random.randn(n, 2)
    dependent = latent.dot(dependency)
    scaled = dependent * scale
    scaled_with_offset = scaled + mu
    # 新しい相関データセットの x と y を返します
    return scaled_with_offset[:, 0], scaled_with_offset[:, 1]
```
