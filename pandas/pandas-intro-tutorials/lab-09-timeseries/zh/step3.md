# 为测量月份添加新列

现在，我们想在数据框中添加一个新列，该列只包含每次测量的月份。这可以使用 `dt` 访问器来实现。

```python
# 为每次测量的月份添加新列
air_quality["month"] = air_quality["datetime"].dt.month
```
