# 设计最佳实践

始终为函数参数赋予简短但有意义的名称。

使用函数的人可能希望采用关键字调用方式。

```python
d = read_prices('prices.csv', debug=True)
```

Python开发工具会在帮助功能和文档中显示这些名称。
