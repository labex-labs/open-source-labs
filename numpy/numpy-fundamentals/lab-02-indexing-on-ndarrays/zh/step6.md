# 扁平迭代器索引

`x.flat` 属性返回一个迭代器，可用于以 C 连续风格遍历整个数组。这个迭代器也可以使用基本切片或高级索引进行索引。

```python
x = np.arange(10)
iterator = x.flat
print(iterator[1:5])  # 输出：[1, 2, 3, 4]
```
