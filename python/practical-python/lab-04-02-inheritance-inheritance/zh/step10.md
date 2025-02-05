# `object` 基类

如果一个类没有父类，你有时会看到使用 `object` 作为基类。

```python
class Shape(object):
...
```

`object` 是 Python 中所有对象的父类。

\*注意：从技术上讲这不是必需的，但你经常会看到它被指定，这是从 Python 2 中它的必需使用方式延续下来的。如果省略，该类仍然会隐式地从 `object` 继承。
