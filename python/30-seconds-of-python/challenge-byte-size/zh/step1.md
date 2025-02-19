# 字符串的字节大小

## 问题

编写一个函数 `byte_size(s)`，它接受一个字符串 `s` 作为输入，并返回其字节大小。字符串的字节大小是将该字符串存储在内存中所需的字节数。要计算字符串的字节大小，你需要使用特定的编码方案对字符串进行编码。在这个挑战中，你将使用 UTF-8 编码方案。

要计算字符串的字节大小，你可以按照以下步骤进行：

1. 使用 UTF-8 编码方案对字符串进行编码。
2. 获取编码后字符串的长度。

你的函数应该返回编码后字符串的长度。

## 示例

```python
byte_size('😀') # 4
byte_size('Hello World') # 11
```

在上面的示例中，字符串 `'😀'` 的字节大小是 4，因为在内存中存储该字符串的 UTF-8 编码版本需要 4 个字节。字符串 `'Hello World'` 的字节大小是 11，因为在内存中存储该字符串的 UTF-8 编码版本需要 11 个字节。
