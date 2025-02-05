# 最终前沿

在练习7.3中，我们实现了如下定义类型检查结构的功能：

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

这背后发生了很多事情。然而，一个令人烦恼的问题是顶部所有那些类型名称的导入（例如，`String`、`PositiveInteger`等）。这正是那种可能导致`from validate import *`语句的情况。关于元类的一个有趣之处在于，它可用于控制类的定义过程。这包括管理类定义本身的环境。让我们来解决那些导入问题。

管理所有验证器名称的第一步是收集它们。打开文件`validate.py`，再次使用涉及`__init_subclass__()`的这段额外代码修改`Validator`基类：

```python
# validate.py

class Validator:
  ...

    # 将所有派生类收集到一个字典中
    validators = { }
    @classmethod
    def __init_subclass__(cls):
        cls.validators[cls.__name__] = cls
```

改动不大，但它正在创建一个包含所有`Validator`子类的小命名空间。看看它：

```python
>>> from validate import Validator
>>> Validator.validators
{'Float': <class 'validate.Float'>,
 'Integer': <class 'validate.Integer'>,
 'NonEmpty': <class 'validate.NonEmpty'>,
 'NonEmptyString': <class 'validate.NonEmptyString'>,
 'Positive': <class 'validate.Positive'>,
 'PositiveFloat': <class 'validate.PositiveFloat'>,
 'PositiveInteger': <class 'validate.PositiveInteger'>,
 'String': <class 'validate.String'>,
 'Typed': <class 'validate.Typed'>}
>>>
```

既然已经完成了这一步，让我们将这个命名空间注入到从`Structure`定义的类的命名空间中。定义以下元类：

```python
# structure.py
...

from validate import Validator
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        methods = methods.maps[0]
        return super().__new__(meta, name, bases, methods)

class Structure(metaclass=StructureMeta):
  ...
```

在这段代码中，`__prepare__()`方法正在创建一个特殊的`ChainMap`映射，它由一个空字典和一个包含所有已定义验证器的字典组成。首先列出的空字典将收集类体中做出的所有定义。`Validator.validators`字典将使所有类型定义可用于作为描述符或参数类型注释。

`__new__()`方法丢弃多余的验证器字典，并将其余定义传递给类型构造函数。这很巧妙，但它让你可以去掉那些烦人的导入：

```python
# stock.py

from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```
