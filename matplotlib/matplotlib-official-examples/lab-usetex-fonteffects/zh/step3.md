# 定义字体函数

在这一步中，我们将定义一个设置字体的函数。该函数接受一个字体名称作为参数，并返回一个将字体设置为指定名称的字符串。

```python
def setfont(font):
    return rf'\font\a {font} at 14pt\a '
```
