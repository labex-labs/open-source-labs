# 数据操作

我们可以对数据框执行诸如排序、应用函数等操作。

```python
# 按轴排序
df.sort_index(axis=1, ascending=False)

# 对数据应用函数
df.apply(np.cumsum)
```
