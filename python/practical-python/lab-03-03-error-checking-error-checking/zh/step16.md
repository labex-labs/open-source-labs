# 练习 3.10：抑制错误

修改 `parse_csv()` 函数，以便在用户明确希望时可以抑制解析错误消息。例如：

```python
>>> portfolio = parse_csv('missing.csv', types=[str,int,float], silence_errors=True)
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}]
>>>
```

在大多数程序中，错误处理是最难做好的事情之一。一般来说，你不应该默默地忽略错误。相反，最好报告问题，并给用户一个选择，如果他们愿意，可以抑制错误消息。
