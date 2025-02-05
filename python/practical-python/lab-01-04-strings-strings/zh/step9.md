# 字节串

一串8位字节，通常在底层I/O中遇到，写法如下：

```python
data = b'Hello World\r\n'
```

通过在第一个引号前加一个小写的b，你指定这是一个字节串，而不是文本串。

大多数常见的字符串操作都适用。

```python
len(data)                         # 13
data[0:5]                         # b'Hello'
data.replace(b'Hello', b'Cruel')  # b'Cruel World\r\n'
```

索引有点不同，因为它返回的字节值是整数。

```python
data[0]   # 72 ('H'的ASCII码)
```

与文本串之间的转换。

```python
text = data.decode('utf-8') # 字节 -> 文本
data = text.encode('utf-8') # 文本 -> 字节
```

`'utf-8'` 参数指定了一种字符编码。其他常见的值包括 `'ascii'` 和 `'latin1'`。
