# 获取和设置选项

我们可以分别使用 `pd.get_option` 或 `pd.set_option` 来获取或设置单个选项的值。在这里，我们将最大显示行数设置为 999。

```python
# 获取当前最大显示行数的设置
print(pd.options.display.max_rows)

# 将最大显示行数设置为 999
pd.options.display.max_rows = 999

# 验证新设置
print(pd.options.display.max_rows)
```
