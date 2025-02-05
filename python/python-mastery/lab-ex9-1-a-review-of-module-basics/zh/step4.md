# 从模块中导入

重启Python并从一个模块中导入选定的符号。

```python
>>> ############### [ RESTART ] ###############
>>> from simplemod import foo
Loaded simplemod
>>> foo()
x is 42
>>>
```

注意这是如何加载整个模块的（观察 `print` 函数的输出以及 `x` 变量是如何被使用的）。

当你使用 `from` 时，模块对象本身是不可见的。例如：

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'simplemod' is not defined
>>>
```

要确保你理解当你从一个模块中导出内容时，它们仅仅是名称引用。例如，试试这个并解释：

```python
>>> from simplemod import x,foo
>>> x
42
>>> foo()
x is 42
>>> x = 13
>>> foo()
x is 42                   #!! 请解释
>>> x
13
>>>
```
