# 理解 Python 生成器

生成器（Generator）是 Python 中一项强大的特性。它们提供了一种简单而优雅的方式来创建迭代器（Iterator）。在 Python 中，当你处理数据序列时，迭代器非常有用，因为它们允许你逐个遍历一系列的值。普通函数通常返回单个值，然后停止执行。然而，生成器不同。它们可以随着时间的推移产生一系列的值，这意味着它们能够逐步产生多个值。

## 什么是生成器？

生成器函数的外观与普通函数相似。但关键区别在于它们返回值的方式。生成器函数不使用 `return` 语句来提供单个结果，而是使用 `yield` 语句。`yield` 语句很特殊。每次执行该语句时，函数的状态会被暂停，并且 `yield` 关键字后面的值会返回给调用者。当再次调用生成器函数时，它会从上次暂停的地方继续执行。

让我们从创建一个简单的生成器函数开始。Python 中的内置 `range()` 函数不支持小数步长。因此，我们将创建一个可以生成具有小数步长的数字范围的生成器函数。

1. 首先，你需要在 WebIDE 中打开一个新的 Python 终端。为此，请点击“Terminal”菜单，然后选择“New Terminal”。
2. 终端打开后，在终端中输入以下代码。这段代码定义了一个生成器函数，然后对其进行测试。

```python
def frange(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step

# Test the generator with a for loop
for x in frange(0, 2, 0.25):
    print(x, end=' ')
```

在这段代码中，`frange` 函数是一个生成器函数。它用 `start` 值初始化变量 `current`。然后，只要 `current` 小于 `stop` 值，它就会产生 `current` 值，然后将 `current` 增加 `step` 值。`for` 循环会遍历 `frange` 生成器函数产生的值并将其打印出来。

你应该会看到以下输出：

```
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

## 生成器的一次性特性

生成器的一个重要特性是它们是可耗尽的。这意味着一旦你遍历了生成器产生的所有值，就不能再用它来产生相同的序列值了。让我们用以下代码来演示这一点：

```python
# Create a generator object
f = frange(0, 2, 0.25)

# First iteration works fine
print("First iteration:")
for x in f:
    print(x, end=' ')
print("\n")

# Second iteration produces nothing
print("Second iteration:")
for x in f:
    print(x, end=' ')
print("\n")
```

在这段代码中，我们首先使用 `frange` 函数创建了一个生成器对象 `f`。第一个 `for` 循环遍历生成器产生的所有值并将其打印出来。第一次迭代之后，生成器已经耗尽，这意味着它已经产生了所有能产生的值。因此，当我们在第二个 `for` 循环中再次尝试遍历它时，它不会产生任何新的值。

输出：

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:

```

注意，第二次迭代没有产生任何输出，因为生成器已经耗尽了。

## 使用类创建可重复使用的生成器

如果你需要多次遍历相同的序列值，可以将生成器封装在一个类中。这样做的话，每次开始新的迭代时，都会创建一个全新的生成器。

```python
class FRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        n = self.start
        while n < self.stop:
            yield n
            n += self.step

# Create an instance
f = FRange(0, 2, 0.25)

# We can iterate multiple times
print("First iteration:")
for x in f:
    print(x, end=' ')
print("\n")

print("Second iteration:")
for x in f:
    print(x, end=' ')
print("\n")
```

在这段代码中，我们定义了一个类 `FRange`。`__init__` 方法初始化 `start`、`stop` 和 `step` 值。`__iter__` 方法是 Python 类中的一个特殊方法，用于创建迭代器。在 `__iter__` 方法内部，我们有一个生成器，它产生值的方式与我们之前定义的 `frange` 函数类似。

当我们创建 `FRange` 类的实例 `f` 并多次对其进行迭代时，每次迭代都会调用 `__iter__` 方法，该方法会创建一个全新的生成器。因此，我们可以多次获取相同的序列值。

输出：

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

这一次，我们可以多次迭代，因为每次调用 `__iter__()` 方法时都会创建一个全新的生成器。
