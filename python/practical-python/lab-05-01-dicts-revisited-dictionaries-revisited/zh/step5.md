# 实例（Instance）与类（Class）

实例和类是相互关联的。`__class__` 属性会指向对应的类。

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{ 'name': 'GOOG', 'shares': 100, 'price': 490.1 }
>>> s.__class__
<class '__main__.Stock'>
>>>
```

实例字典保存着每个实例独有的数据，而类字典保存着 _所有_ 实例共同共享的数据。
