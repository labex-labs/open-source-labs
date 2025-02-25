# データの作成

次に、ビジュアライゼーションで使用するランダムなデータを作成します。この例では、numpyを使って2つのランダムなデータの配列を作成します。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.random.rand(20)
y = 1e7 * np.random.rand(20)
```
