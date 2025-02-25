# クロス集計

クロス集計は、複数の変数間の関係を定量的に分析する方法です。

```python
# Cross tabulation between row and col
df.pivot_table(index="row", columns="col", fill_value=0, aggfunc="size")
```
