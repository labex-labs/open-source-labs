# 合成データセットの生成

`X`と`y`が線形に関連付けられた合成データセットを生成します。`X`の 10 個の特徴量を使って`y`を生成します。他の特徴量は`y`の予測には役立ちません。また、`n_samples == n_features`のデータセットも生成します。このような設定は OLS モデルにとってチャレンジングであり、潜在的に任意の大きな重みをもたらす可能性があります。重みに事前分布を持ち、ペナルティを課すことで問題を軽減します。最後に、ガウスノイズを追加します。

```python
from sklearn.datasets import make_regression

X, y, true_weights = make_regression(
    n_samples=100,
    n_features=100,
    n_informative=10,
    noise=8,
    coef=True,
    random_state=42,
)
```
