# データを準備する

分類用の合成データを生成します。分類対象の関数は以下のように定義されます。

```python
def g(x):
    """The function to predict (classification will then consist in predicting
    whether g(x) <= 0 or not)"""
    return 5.0 - x[:, 1] - 0.5 * x[:, 0] ** 2.0
```

次に、実験のデザインと観測値を作成する必要があります。

```python
# A few constants
lim = 8

# Design of experiments
X = np.array(
    [
        [-4.61611719, -6.00099547],
        [4.10469096, 5.32782448],
        [0.00000000, -0.50000000],
        [-6.17289014, -4.6984743],
        [1.3109306, -6.93271427],
        [-5.03823144, 3.10584743],
        [-2.87600388, 6.74310541],
        [5.21301203, 4.26386883],
    ]
)

# Observations
y = np.array(g(X) > 0, dtype=int)
```
