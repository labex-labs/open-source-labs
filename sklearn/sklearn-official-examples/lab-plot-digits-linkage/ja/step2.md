# データセットの読み込みと準備

手書き数字データセットを読み込み、データとターゲットラベルを抽出することでクラスタリングのために準備します。再現性を保証するため、乱数シードをゼロに設定します。

```python
digits = datasets.load_digits()
X, y = digits.data, digits.target
n_samples, n_features = X.shape
np.random.seed(0)
```
