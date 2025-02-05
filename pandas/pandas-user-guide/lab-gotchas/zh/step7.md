# 处理字节序问题

在处理由字节序不同的机器创建的数据时，你可能会遇到字节序问题。在将数据传递给 Pandas 之前，将其转换为本机系统字节序。

```python
x = np.array(list(range(10)), ">i4")  # 大端序
newx = x.byteswap().newbyteorder()  # 强制转换为本机字节序
s = pd.Series(newx)
```
