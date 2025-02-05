# 使用多个聚合进行透视

我们还可以在透视操作中执行多个聚合。

```python
# 使用 val0 的均值和总和对 df 进行透视
df.pivot_table(values="val0", index="row", columns="col", aggfunc=["mean", "sum"])
```
