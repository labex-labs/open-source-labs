# ランダムなデータの生成

散布図とヒストグラムに使用するために、いくつかのランダムなデータを生成します。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.random.randn(1000)
y = np.random.randn(1000)
```
