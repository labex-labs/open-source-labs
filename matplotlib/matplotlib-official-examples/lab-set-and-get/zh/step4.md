# 获取属性

我们可以使用 `getp` 方法来获取对象的属性。我们可以用它来查询单个属性的值：

```python
plt.getp(line, 'linewidth')
```

这将返回线条对象的线宽属性的值。

我们也可以使用 `getp` 来获取对象的所有属性/值对：

```python
plt.getp(line)
```

这将返回所有属性及其值的长列表。
