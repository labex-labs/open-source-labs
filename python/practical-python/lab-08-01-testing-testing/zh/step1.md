# 断言

`assert` 语句是程序的内部检查。如果表达式不为真，它会引发 `AssertionError` 异常。

`assert` 语句语法。

```python
assert <表达式> [, '诊断消息']
```

例如。

```python
assert isinstance(10, int), '预期为整数'
```

它不应用于检查用户输入（即网页表单上输入的数据等）。它的目的更多是用于内部检查和不变量（应该始终为真的条件）。
