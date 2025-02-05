# 使用 enumerate() 进行计数

如果你在迭代时需要保留一个计数器或索引，`enumerate()` 是一个很有用的函数。例如，假设你想要一个额外的行号：

```python
>>> for rowno, row in enumerate(rows):
        print(rowno, row)

0 ['AA', '100', '32.20']
1 ['IBM', '50', '91.10']
2 ['CAT', '150', '83.44']
3 ['MSFT', '200', '51.23']
4 ['GE', '95', '40.37']
5 ['MSFT', '50', '65.10']
6 ['IBM', '100', '70.44']
>>>
```

如果你注意结构的组织方式，可以将其与解包结合使用：

```python
>>> for rowno, (name, shares, price) in enumerate(rows):
        print(rowno, name, shares, price)

0 AA 100 32.20
1 IBM 50 91.10
2 CAT 150 83.44
3 MSFT 200 51.23
4 GE 95 40.37
5 MSFT 50 65.10
6 IBM 100 70.44
>>>
```
