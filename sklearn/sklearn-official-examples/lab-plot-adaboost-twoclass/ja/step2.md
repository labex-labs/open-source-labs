# データセットを構築する

このステップでは、`sklearn.datasets`モジュールの`make_gaussian_quantiles`関数を使って、2 つのガウス分布によるクラスターから構成される非線形分離可能な分類データセットを作成します。また、2 つのクラスターを連結して、それぞれにラベルを割り当てます。

```python
X1, y1 = make_gaussian_quantiles(
    cov=2.0, n_samples=200, n_features=2, n_classes=2, random_state=1
)
X2, y2 = make_gaussian_quantiles(
    mean=(3, 3), cov=1.5, n_samples=300, n_features=2, n_classes=2, random_state=1
)
X = np.concatenate((X1, X2))
y = np.concatenate((y1, -y2 + 1))
```
