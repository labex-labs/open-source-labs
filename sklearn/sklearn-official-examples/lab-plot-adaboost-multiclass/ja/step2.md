# データセットを読み込む

`sklearn.datasets` からの `make_gaussian_quantiles` 関数を使ってデータセットを生成します。この関数は等方性ガウス分布を生成し、クラス間に分離を追加して問題を難しくします。

```python
X, y = make_gaussian_quantiles(
    n_samples=13000, n_features=10, n_classes=3, random_state=1
)
```
