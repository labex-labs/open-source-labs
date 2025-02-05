# 设置属性

pyplot 接口允许我们设置和获取用于可视化数据的对象属性。我们可以使用 `setp` 方法来设置对象的属性。例如，要将线条的线型设置为虚线，我们使用以下代码：

```python
line, = plt.plot([1, 2, 3])
plt.setp(line, linestyle='--')
```

如果我们想知道有效参数类型，可以在不提供值的情况下提供要设置的属性名称：

```python
plt.setp(line, 'linestyle')
```

这将返回以下输出：

```
linestyle: {'-', '--', '-.', ':', '', (offset, on-off-seq),...}
```

如果我们想查看所有可以设置的属性及其可能的值，可以使用以下代码：

```python
plt.setp(line)
```

这将返回一个包含属性及其可能值的长列表。
