# 使用单一聚合进行透视

透视（Pivot）是 Pandas 中重塑数据的关键方法之一。它提供了一种转换数据的方式，以便你可以从不同角度查看数据。

```python
# 使用 val0 的均值对 df 进行透视
df.pivot_table(values="val0", index="row", columns="col", aggfunc="mean", fill_value=0)
```
