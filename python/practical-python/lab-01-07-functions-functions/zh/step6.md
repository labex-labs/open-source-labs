# 练习 1.29：定义一个函数

尝试定义一个简单的函数：

```python
>>> def greeting(name):
        'Issues a greeting'
        print('Hello', name)

>>> greeting('Guido')
Hello Guido
>>> greeting('Paula')
Hello Paula
>>>
```

如果函数的第一行语句是一个字符串，那么它将作为文档。尝试输入诸如 `help(greeting)` 这样的命令来查看它的显示内容。
