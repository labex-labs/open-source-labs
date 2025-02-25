# DataFrame の作成

もう 1 つの基本的なデータ構造は DataFrame です。これは、潜在的に異なる型の列を持つ 2 次元のラベル付きデータ構造です。

```python
# Create a DataFrame
df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
```
