# 将宽表格格式转换为长表格格式

现在，让我们使用 `melt` 函数将二氧化氮（𝑁𝑂2）的宽格式数据转换为长格式。

```python
# 重置 no2_pivoted 的索引
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

# 转换数据格式
no_2 = no2_pivoted.melt(id_vars="date.utc")
```
