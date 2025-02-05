# 将列标签转换为小写

最后，我们将使用一个函数把列标签转换为小写。

```python
# 将列标签转换为小写
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
```
