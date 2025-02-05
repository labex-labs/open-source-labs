# 保存和加载数据

Pandas 提供了以各种格式（如 csv、excel、hdf5 等）保存和加载数据的方法。

```python
# 将数据保存到 csv 文件
df.to_csv("foo.csv")

# 从 csv 文件加载数据
pd.read_csv("foo.csv")
```
