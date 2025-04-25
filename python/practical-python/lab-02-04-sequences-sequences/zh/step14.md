# 练习 2.15：一个实用的 enumerate() 示例

回想一下，文件`missing.csv`包含一个股票投资组合的数据，但有一些行的数据缺失。使用`enumerate()`，修改你的`pcost.py`程序，使其在遇到错误输入时打印出行号和警告信息。

```python
>>> cost = portfolio_cost('/home/labex/project/missing.csv')
第4行：无法转换：['MSFT', '', '51.23']
第7行：无法转换：['IBM', '', '70.44']
>>>
```

要做到这一点，你需要修改代码的几个部分。

```python
...
for rowno, row in enumerate(rows, start=1):
    try:
     ...
    except ValueError:
        print(f'第{rowno}行：错误的行：{row}')
```
