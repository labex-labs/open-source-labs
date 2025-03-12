# 限制属性名称

目前，我们的 `Structure` 类允许在其实例上设置任何属性。对于初学者来说，这一开始可能看起来很方便，但实际上会导致很多问题。当你使用一个类时，你期望某些属性存在并以特定方式使用。如果用户拼写错误属性名，或者尝试设置并非原始设计一部分的属性，可能会导致难以发现的错误。

## 属性限制的必要性

让我们看一个简单的场景，来理解为什么需要限制属性名称。考虑以下代码：

```python
s = Stock('GOOG', 100, 490.1)
s.shares = 50      # Correct attribute name
s.share = 60       # Typo in attribute name - creates a new attribute instead of updating
```

在第二行中，有一个拼写错误。我们写的是 `share` 而不是 `shares`。在 Python 中，它不会引发错误，而是会简单地创建一个名为 `share` 的新属性。这可能会导致难以察觉的错误，因为你可能以为自己在更新 `shares` 属性，但实际上是在创建一个新属性。这会使你的代码行为异常，并且很难调试。

## 实现属性限制

为了解决这个问题，我们可以重写 `__setattr__` 方法。每当你尝试在对象上设置属性时，都会调用这个方法。通过重写它，我们可以控制哪些属性可以设置，哪些不可以。

用以下代码更新 `structure.py` 中的 `Structure` 类：

```python
def __setattr__(self, name, value):
    """
    Restrict attribute setting to only those defined in _fields
    or attributes starting with underscore (private attributes).
    """
    if name.startswith('_'):
        # Allow setting private attributes (starting with '_')
        super().__setattr__(name, value)
    elif name in self._fields:
        # Allow setting attributes defined in _fields
        super().__setattr__(name, value)
    else:
        # Raise an error for other attributes
        raise AttributeError(f'No attribute {name}')
```

这个方法的工作原理如下：

1. 如果属性名以下划线 (`_`) 开头，则被视为私有属性。私有属性通常用于类的内部用途。我们允许设置这些属性，因为它们是类内部实现的一部分。
2. 如果属性名在 `_fields` 列表中，这意味着它是类设计中定义的属性之一。我们允许设置这些属性，因为它们是类预期行为的一部分。
3. 如果属性名不满足上述任何一个条件，我们会引发一个 `AttributeError`。这会告诉用户，他们正在尝试设置一个类中不存在的属性。

## 测试属性限制

现在我们已经实现了属性限制，让我们测试一下，确保它按预期工作。创建一个名为 `test_attributes.py` 的文件，内容如下：

```python
# test_attributes.py
from structure import Stock

s = Stock('GOOG', 100, 490.1)

# This should work - valid attribute
print("Setting shares to 50")
s.shares = 50
print(f"Shares is now: {s.shares}")

# This should work - private attribute
print("\nSetting _internal_data")
s._internal_data = "Some data"
print(f"_internal_data is: {s._internal_data}")

# This should fail - invalid attribute
print("\nTrying to set an invalid attribute:")
try:
    s.share = 60  # Typo in attribute name
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

要运行测试，请打开终端并输入以下命令：

```bash
python3 test_attributes.py
```

你应该会看到以下输出：

```
Setting shares to 50
Shares is now: 50

Setting _internal_data
_internal_data is: Some data

Trying to set an invalid attribute:
Error correctly caught: No attribute share
```

这个输出表明，我们的类现在可以防止意外的属性错误。它允许我们设置有效的属性和私有属性，但当我们尝试设置无效属性时会引发错误。

## 属性限制的价值

限制属性名称对于编写健壮且可维护的代码非常重要。原因如下：

1. 它有助于捕获属性名的拼写错误。如果你在输入属性名时出错，代码会引发错误，而不是创建一个新属性。这使得在开发过程的早期更容易发现和修复错误。
2. 它可以防止尝试设置类设计中不存在的属性。这确保了类按预期使用，并且代码行为可预测。
3. 它避免了意外创建新属性。创建新属性可能会导致意外行为，使代码更难理解和维护。

通过限制属性名称，我们使代码更可靠，更易于处理。
