# 注释

当你开始使用解释器进行实验时，你通常想了解更多关于不同对象支持的操作。例如，你如何找出字符串上可用的操作？

根据你的 Python 环境，你可能可以通过按 Tab 键补全来查看可用方法的列表。例如，尝试输入以下内容：

```python
>>> s = 'hello world'
>>> s.<tab键>
>>>
```

如果按 Tab 键没有任何反应，你可以使用内置的 `dir()` 函数。例如：

```python
>>> s = 'hello'
>>> dir(s)
['__add__', '__class__', '__contains__',..., 'find', 'format',
'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip','split','splitlines','startswith','strip','swapcase',
'title', 'translate', 'upper', 'zfill']
>>>
```

`dir()` 会生成一个可以出现在 `(.)` 之后的所有操作的列表。使用 `help()` 命令获取有关特定操作的更多信息：

```python
>>> help(s.upper)
关于内置函数upper的帮助文档：

upper(...)
    S.upper() -> string

    返回字符串S转换为大写后的副本。
>>>
```
