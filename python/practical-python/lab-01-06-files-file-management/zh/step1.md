# 文件输入与输出

打开一个文件。

```python
f = open('foo.txt', 'rt')     # 以读取模式（文本）打开
g = open('bar.txt', 'wt')     # 以写入模式（文本）打开
```

读取所有数据。

```python
data = f.read()

# 最多读取'maxbytes' 字节的数据
data = f.read([maxbytes])
```

写入一些文本。

```python
g.write('some text')
```

完成后关闭文件。

```python
f.close()
g.close()
```

文件应该正确关闭，但这很容易被遗忘。因此，推荐的方法是像这样使用 `with` 语句。

```python
with open(filename, 'rt') as file:
    # 使用文件 `file`
  ...
    # 无需显式关闭
...语句
```

当控制离开缩进的代码块时，这会自动关闭文件。
