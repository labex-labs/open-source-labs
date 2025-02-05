# 类的作用

构成类定义的那些定义由该类的所有实例共享。注意，所有实例都有一个指向其关联类的链接：

```python
>>> goog.__class__
... 查看输出...
>>> ibm.__class__
... 查看输出...
>>>
```

尝试在实例上调用一个方法：

```python
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
>>>
```

注意，“cost”这个名字在 `goog.__dict__` 或 `ibm.__dict__` 中都没有定义。相反，它是由类字典提供的。试试这个：

```python
>>> SimpleStock.__dict__['cost']
... 查看输出...
>>>
```

尝试直接通过字典调用 `cost()` 方法：

```python
>>> SimpleStock.__dict__['cost'](goog)
49010.00
>>> SimpleStock.__dict__['cost'](ibm)
4561.5
>>>
```

注意你是如何调用类定义中定义的函数的，以及 `self` 参数是如何获取实例的。

如果你向类中添加一个新值，它就会变成一个对所有实例都可见的类变量。试试看：

```python
>>> SimpleStock.spam = 42
>>> ibm.spam
42
>>> goog.spam
42
>>>
```

观察到 `spam` 不是实例字典的一部分。

```python
>>> ibm.__dict__
... 查看输出...
>>>
```

相反，它是类字典的一部分：

```python
>>> SimpleStock.__dict__['spam']
42
>>>
```

本质上，这就是类的全部——它是实例共享的值的集合。
