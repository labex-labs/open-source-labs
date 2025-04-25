# 练习 1.18：正则表达式

基本字符串操作的一个局限性在于它们不支持任何高级模式匹配。为此，你需要使用 Python 的 `re` 模块和正则表达式。正则表达式处理是一个很大的主题，但这里有一个简短的示例：

```python
>>> text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
>>> # 查找所有日期出现的位置
>>> import re
>>> re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']
>>> # 用替换文本替换所有日期出现的位置
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'
>>>
```

有关 `re` 模块的更多信息，请参阅官方文档 [https://docs.python.org/library/re.html](https://docs.python.org/3/library/re.html)。
