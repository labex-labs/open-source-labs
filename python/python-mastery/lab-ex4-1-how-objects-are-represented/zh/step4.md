# 理解类和实例之间的关系

现在，我们将探索在 Python 中类和实例是如何关联的，以及方法查找是如何工作的。这是一个重要的概念，因为它能帮助你理解在处理对象时，Python 是如何查找和使用方法及属性的。

首先，让我们检查一下我们的实例属于哪个类。了解实例所属的类至关重要，因为它能告诉我们 Python 会在哪里查找与该实例相关的方法和属性。

```python
>>> goog.__class__
<class '__main__.SimpleStock'>
>>> ibm.__class__
<class '__main__.SimpleStock'>
```

这两个实例都有一个指向 `SimpleStock` 类的引用。这个引用就像一个指针，Python 在需要查找方法时会使用它。当你在一个实例上调用方法时，Python 会使用这个引用来找到合适的方法定义。

当你在一个实例上调用方法时，Python 会遵循以下步骤：

1. 它会在实例的 `__dict__` 中查找该属性。实例的 `__dict__` 就像一个存储区域，所有特定于该实例的属性都保存在这里。
2. 如果没有找到，它会检查类的 `__dict__`。类的 `__dict__` 存储了该类所有实例共有的所有属性和方法。
3. 如果在类中找到该属性，就返回该属性。

让我们来实际看一下。首先，验证 `cost` 方法不在实例字典中。这一步有助于我们理解 `cost` 方法不是每个实例特有的，而是在类级别定义的。

```python
>>> 'cost' in goog.__dict__
False
>>> 'cost' in ibm.__dict__
False
```

那么 `cost` 方法是从哪里来的呢？让我们检查一下类。通过查看类的 `__dict__`，我们可以找出 `cost` 方法的定义位置。

```python
>>> SimpleStock.__dict__['cost']
<function SimpleStock.cost at 0x7f...>
```

该方法是在类中定义的，而不是在实例中。当你调用 `goog.cost()` 时，Python 在 `goog.__dict__` 中找不到 `cost`，所以它会在 `SimpleStock.__dict__` 中查找并在那里找到它。

实际上，你可以直接从类字典中调用方法，将实例作为第一个参数传递（这个参数会变成 `self`）。这展示了 Python 在你使用普通的 `instance.method()` 语法时是如何在内部调用方法的。

```python
>>> SimpleStock.__dict__['cost'](goog)
49010.0
>>> SimpleStock.__dict__['cost'](ibm)
4561.5
```

这本质上就是你调用 `goog.cost()` 时 Python 在幕后所做的事情。

现在，让我们添加一个类属性。类属性由所有实例共享。这意味着该类的所有实例都可以访问这个属性，并且它只在类级别存储一次。

```python
>>> SimpleStock.exchange = 'NASDAQ'
>>> goog.exchange
'NASDAQ'
>>> ibm.exchange
'NASDAQ'
```

两个实例都可以访问 `exchange` 属性，但它并不存储在它们各自的字典中。让我们通过检查实例和类的字典来验证这一点。

```python
>>> 'exchange' in goog.__dict__
False
>>> 'exchange' in SimpleStock.__dict__
True
>>> SimpleStock.__dict__['exchange']
'NASDAQ'
```

这表明：

1. 类属性由所有实例共享。所有实例都可以访问同一个类属性，而无需拥有自己的副本。
2. Python 首先检查实例字典，然后检查类字典。这是 Python 在你尝试在实例上访问属性时查找属性的顺序。
3. 类充当共享数据和行为（方法）的存储库。类存储了所有实例都可以使用的所有公共属性和方法。

如果我们修改一个具有相同名称的实例属性，它会遮蔽类属性。这意味着当你在该实例上访问该属性时，Python 将使用特定于该实例的值，而不是类级别的值。

```python
>>> ibm.exchange = 'NYSE'
>>> ibm.exchange
'NYSE'
>>> goog.exchange  # 仍然使用类属性
'NASDAQ'
>>> ibm.__dict__['exchange']
'NYSE'
```

现在 `ibm` 有了自己的 `exchange` 属性，它遮蔽了类属性，而 `goog` 仍然使用类属性。
