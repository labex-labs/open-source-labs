# 理解单继承和多继承

在这一步中，我们将学习 Python 中两种主要的继承类型：单继承和多继承。继承是面向对象编程中的一个基本概念，它允许一个类从其他类继承属性和方法。我们还将探讨当有多个候选方法时，Python 如何确定调用哪个方法，这个过程称为方法解析。

## 单继承

单继承是指类形成单一的继承链。可以将其想象成一个家族树，每个类只有一个直接父类。让我们创建一个示例来理解它的工作原理。

首先，在 WebIDE 中打开一个新的终端。终端打开后，输入以下命令并按回车键启动 Python 解释器：

```bash
python3
```

现在你已经进入了 Python 解释器，我们将创建三个形成单继承链的类。输入以下代码：

```python
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

class C(B):
    def spam(self):
        print('C.spam')
        super().spam()
```

在这段代码中，类 `B` 继承自类 `A`，类 `C` 继承自类 `B`。`super()` 函数用于调用父类的方法。

定义这些类之后，我们可以找出 Python 搜索方法的顺序。这个顺序称为方法解析顺序（Method Resolution Order，MRO）。要查看类 `C` 的 MRO，请输入以下代码：

```python
C.__mro__
```

你应该会看到类似以下的输出：

```
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

这个输出表明，Python 首先在类 `C` 中查找方法，然后在类 `B` 中查找，接着在类 `A` 中查找，最后在基类 `object` 中查找。

现在，让我们创建类 `C` 的一个实例并调用其 `spam()` 方法。输入以下代码：

```python
c = C()
c.spam()
```

你应该会看到以下输出：

```
C.spam
B.spam
A.spam
```

这个输出展示了 `super()` 在单继承链中的工作方式。当 `C.spam()` 调用 `super().spam()` 时，它调用的是 `B.spam()`。然后，当 `B.spam()` 调用 `super().spam()` 时，它调用的是 `A.spam()`。

## 多继承

多继承允许一个类从多个父类继承。这使得一个类可以访问其所有父类的属性和方法。让我们看看在这种情况下方法解析是如何工作的。

在 Python 解释器中输入以下代码：

```python
class Base:
    def spam(self):
        print('Base.spam')

class X(Base):
    def spam(self):
        print('X.spam')
        super().spam()

class Y(Base):
    def spam(self):
        print('Y.spam')
        super().spam()

class Z(Base):
    def spam(self):
        print('Z.spam')
        super().spam()
```

现在，我们将创建一个类 `M`，它继承自多个父类 `X`、`Y` 和 `Z`。输入以下代码：

```python
class M(X, Y, Z):
    pass

M.__mro__
```

你应该会看到以下输出：

```
(<class '__main__.M'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.Base'>, <class 'object'>)
```

这个输出显示了类 `M` 的方法解析顺序。Python 将按照这个顺序搜索方法。

让我们创建类 `M` 的一个实例并调用其 `spam()` 方法：

```python
m = M()
m.spam()
```

你应该会看到以下输出：

```
X.spam
Y.spam
Z.spam
Base.spam
```

请注意，`super()` 并不只是调用直接父类的方法。相反，它遵循子类定义的方法解析顺序（MRO）。

让我们以不同的顺序指定父类来创建另一个类 `N`：

```python
class N(Z, Y, X):
    pass

N.__mro__
```

你应该会看到以下输出：

```
(<class '__main__.N'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.Base'>, <class 'object'>)
```

现在，创建类 `N` 的一个实例并调用其 `spam()` 方法：

```python
n = N()
n.spam()
```

你应该会看到以下输出：

```
Z.spam
Y.spam
X.spam
Base.spam
```

这展示了一个重要的概念：在 Python 的多继承中，类定义中父类的顺序决定了方法解析顺序。无论从哪个类调用 `super()` 函数，它都会遵循这个顺序。

当你完成对这些概念的探索后，可以输入以下代码退出 Python 解释器：

```python
exit()
```
