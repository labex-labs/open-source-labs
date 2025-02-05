# 使用缺失值和填充值

`missing_values` 和 `filling_values` 参数用于处理缺失数据。`missing_values` 参数用于识别缺失数据，而 `filling_values` 参数用于为缺失的条目提供一个值。

```python
np.genfromtxt(StringIO(data), missing_values="N/A", filling_values=0)
```
