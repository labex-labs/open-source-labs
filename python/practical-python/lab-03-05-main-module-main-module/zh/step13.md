# 练习 3.15：`main()` 函数

在 `report.py` 文件中添加一个 `main()` 函数，该函数接受命令行选项列表并产生与之前相同的输出。你应该能够像这样交互式地运行它：

```python
>>> import report
>>> report.main(['/home/labex/project/report.py', '/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv'])
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

修改 `pcost.py` 文件，使其具有类似的 `main()` 函数：

```python
>>> import pcost
>>> pcost.main(['/home/labex/project/pcost.py', '/home/labex/project/portfolio.csv'])
Total cost: 44671.15
>>>
```
