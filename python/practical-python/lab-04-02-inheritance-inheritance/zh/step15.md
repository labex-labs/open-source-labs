# 练习 4.8：整合所有内容

修改 `report.py` 程序，使 `portfolio_report()` 函数接受一个可选参数来指定输出格式。例如：

```python
>>> report.portfolio_report('portfolio.csv', 'prices.csv', 'txt')
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```

修改主程序，以便可以在命令行中给出格式：

```bash
$ python3 report.py portfolio.csv prices.csv csv
Name,Shares,Price,Change
AA,100,9.22,-22.98
IBM,50,106.28,15.18
CAT,150,35.46,-47.98
MSFT,200,20.89,-30.34
GE,95,13.48,-26.89
MSFT,50,20.89,-44.21
IBM,100,106.28,35.84
$
```
