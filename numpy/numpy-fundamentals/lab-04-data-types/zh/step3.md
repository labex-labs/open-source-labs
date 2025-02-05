# 获取数组的数据类型

要确定数组的数据类型，可以访问 `dtype` 属性。例如：

```python
z.dtype
# 返回数组 z 的数据类型，即 uint8
```

`dtype` 对象还包含有关该类型的信息，例如其位宽和字节顺序。可以使用 `dtype` 对象查询类型的属性，例如它是否为整数。例如：

```python
d = np.dtype(int)
# 创建一个用于 int 的 dtype 对象

np.issubdtype(d, np.integer)
# 返回 True，表示 d 是 np.integer 的子数据类型

np.issubdtype(d, np.floating)
# 返回 False，表示 d 不是 np.floating 的子数据类型
```
