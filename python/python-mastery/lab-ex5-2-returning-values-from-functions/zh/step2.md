# 返回可选值

有时，一个函数可能会返回一个可选值 —— 这可能是一种表示成功或失败的机制。最常见的约定是使用 `None` 来表示缺失值。修改上面的 `parse_line()` 函数，使其在成功时返回一个元组，在数据错误时返回 `None`。例如：

```python
>>> parse_line('email=guido@python.org')
('email', 'guido@python.org')
>>> parse_line('spam')       # 返回 None
>>>
```

设计讨论：对于 `parse_line()` 函数来说，在数据格式错误时引发异常会更好吗？
