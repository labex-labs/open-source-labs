# 乱数シードとビンの設定

再現性のために乱数シードを設定し、ビンの端を固定します。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Fixing bin edges
HIST_BINS = np.linspace(-4, 4, 100)
```
