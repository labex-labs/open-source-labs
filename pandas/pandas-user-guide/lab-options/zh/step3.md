# 重置选项

如果我们希望将一个或多个选项重置为其默认值，可以使用 `pd.reset_option`。

```python
# 将最大显示行数重置为默认值
pd.reset_option("display.max_rows")

# 验证重置
print(pd.options.display.max_rows)
```
