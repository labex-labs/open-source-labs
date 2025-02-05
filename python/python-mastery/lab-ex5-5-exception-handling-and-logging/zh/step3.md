# 日志记录

修改代码，以便使用`logging`模块发出警告消息。此外，提供可选的调试信息，指出失败的原因。例如：

```python
>>> import reader
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG)
>>> port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
警告:reader:第4行：错误的行：['C', '', '53.08']
调试:reader:第4行：原因：基数为10的int()的无效文字：''
警告:reader:第7行：错误的行：['DIS', '50', 'N/A']
调试:reader:第7行：原因：无法将字符串转换为浮点数：'N/A'
警告:reader:第8行：错误的行：['GE', '', '37.23']
调试:reader:第8行：原因：基数为10的int()的无效文字：''
警告:reader:第13行：错误的行：['INTC', '', '21.84']
调试:reader:第13行：原因：基数为10的int()的无效文字：''
警告:reader:第17行：错误的行：['MCD', '', '51.11']
调试:reader:第17行：原因：基数为10的int()的无效文字：''
警告:reader:第19行：错误的行：['MO', '', '70.09']
调试:reader:第19行：原因：基数为10的int()的无效文字：''
警告:reader:第22行：错误的行：['PFE', '', '26.40']
调试:reader:第22行：原因：基数为10的int()的无效文字：''
警告:reader:第26行：错误的行：['VZ', '', '42.92']
调试:reader:第26行：原因：基数为10的int()的无效文字：''
>>>
```
