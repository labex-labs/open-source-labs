# 打印

`print` 函数会输出一行包含所传递值的文本。

```python
print('Hello world!') # 输出文本 'Hello world!'
```

你可以使用变量。打印的文本将是变量的值，而非变量名。

```python
x = 100
print(x) # 输出文本 '100'
```

如果你向 `print` 传递多个值，它们会用空格分隔。

```python
name = 'Jake'
print('My name is', name) # 输出文本 'My name is Jake'
```

`print()` 总是会在末尾添加一个换行符。

```python
print('Hello')
print('My name is', 'Jake')
```

这将输出：

```code
Hello
My name is Jake
```

可以抑制额外的换行符：

```python
print('Hello', end=' ')
print('My name is', 'Jake')
```

这段代码现在将输出：

```code
Hello My name is Jake
```
