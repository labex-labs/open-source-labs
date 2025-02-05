# 生成器表达式

列表推导式的生成器版本。

```python
>>> a = [1,2,3,4]
>>> b = (2*x for x in a)
>>> b
<generator object at 0x58760>
>>> for i in b:
...   print(i, end=' ')
...
2 4 6 8
>>>
```

与列表推导式的区别：

- 不构建列表。
- 唯一有用的目的是迭代。
- 一旦被消耗，就不能再使用。

通用语法：

```python
(<表达式> for i in s if <条件>)
```

它也可以用作函数参数：

```python
sum(x*x for x in a)
```

它可以应用于任何可迭代对象：

```python
>>> a = [1,2,3,4]
>>> b = (x*x for x in a)
>>> c = (-x for x in b)
>>> for i in c:
...   print(i, end=' ')
...
-1 -4 -9 -16
>>>
```

生成器表达式的主要用途是在对序列执行某些计算但只使用结果一次的代码中。例如，从文件中去除所有注释：

```python
f = open('somefile.txt')
lines = (line for line in f if not line.startswith('#'))
for line in lines:
  ...
f.close()
```

使用生成器，代码运行得更快且占用内存少。它就像应用于流的过滤器。
