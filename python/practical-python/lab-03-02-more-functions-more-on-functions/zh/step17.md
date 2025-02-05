# 练习3.7：选择不同的列分隔符

虽然CSV文件相当常见，但你也可能会遇到使用不同列分隔符的文件，比如制表符或空格。例如，`portfolio.dat` 文件看起来是这样的：

```csv
name shares price
"AA" 100 32.20
"IBM" 50 91.10
"CAT" 150 83.44
"MSFT" 200 51.23
"GE" 95 40.37
"MSFT" 50 65.10
"IBM" 100 70.44
```

`csv.reader()` 函数允许指定不同的列分隔符，如下所示：

```python
rows = csv.reader(f, delimiter=' ')
```

修改你在 `/home/labex/project/fileparse_3.7.py` 中的 `parse_csv()` 函数，使其也能允许更改分隔符。

例如：

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.dat', types=[str, int, float], delimiter=' ')
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]
>>>
```
