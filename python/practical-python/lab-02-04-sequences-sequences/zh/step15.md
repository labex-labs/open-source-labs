# 练习 2.16：使用 zip() 函数

在文件`portfolio.csv`中，第一行包含列标题。在之前所有的代码中，我们都忽略了它们。

```python
>>> f = open('/home/labex/project/portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name','shares', 'price']
>>>
```

然而，如果你能将这些标题用于一些有用的事情呢？这就是`zip()`函数发挥作用的地方。首先尝试这样做，将文件标题与一行数据配对：

```python
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> list(zip(headers, row))
[ ('name', 'AA'), ('shares', '100'), ('price', '32.20') ]
>>>
```

注意`zip()`是如何将列标题与列值配对的。我们在这里使用`list()`将结果转换为列表，以便你能看到它。通常，`zip()`创建一个迭代器，必须通过`for`循环来使用它。

这种配对是构建字典的中间步骤。现在试试这个：

```python
>>> record = dict(zip(headers, row))
>>> record
{'price': '32.20', 'name': 'AA','shares': '100'}
>>>
```

这种转换是处理大量数据文件时最有用的技巧之一。例如，假设你想让`pcost.py`程序适用于各种输入文件，而不考虑名称、股票数量和价格所在的实际列号。

修改`pcost.py`中的`portfolio_cost()`函数，使其如下所示：

```python
# pcost.py

def portfolio_cost(filename):
  ...
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # 这捕获了上面 int() 和 float() 转换中的错误
            except ValueError:
                print(f'第{rowno}行：错误的行：{row}')
  ...
```

现在，在一个完全不同的数据文件`portfoliodate.csv`上尝试你的函数，该文件如下所示：

```csv
name,date,time,shares,price
"AA","6/11/2007","9:50am",100,32.20
"IBM","5/13/2007","4:20pm",50,91.10
"CAT","9/23/2006","1:30pm",150,83.44
"MSFT","5/17/2007","10:30am",200,51.23
"GE","2/1/2006","10:45am",95,40.37
"MSFT","10/31/2006","12:05pm",50,65.10
"IBM","7/9/2006","3:15pm",100,70.44
```

```python
>>> portfolio_cost('/home/labex/project/portfoliodate.csv')
44671.15
>>>
```

如果你做对了，你会发现即使数据文件的列格式与之前完全不同，你的程序仍然可以工作。这很酷！

这里所做的更改很细微，但很重要。`portfolio_cost()`不再硬编码为读取单一固定文件格式，新版本可以读取任何 CSV 文件并从中提取感兴趣的值。只要文件有所需的列，代码就会起作用。

修改你在 2.3 节中编写的`report.py`程序，使其使用相同的技术来提取列标题。

尝试在`portfoliodate.csv`文件上运行`report.py`程序，看看它是否能产生与之前相同的答案。
