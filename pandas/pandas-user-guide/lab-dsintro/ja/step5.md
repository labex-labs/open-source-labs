# データの整列と算術演算

データの整列は pandas の重要な機能です。2 つのオブジェクトに対して演算を行うとき、pandas は関連付けられたラベルに基づいてそれらを整列させます。

```python
# Create two DataFrames
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])

# Perform addition operation
result = df1 + df2
```
