# 缩进最佳实践

- 使用空格而非制表符。
- 每级缩进使用 4 个空格。
- 使用支持 Python 的编辑器。

Python 唯一的要求是同一代码块内的缩进需保持一致。例如，这是一个错误示例：

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
        day = day + 1 # 错误
    num_bills = num_bills * 2
```
