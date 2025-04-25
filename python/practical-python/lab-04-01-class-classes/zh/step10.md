# 练习 4.4：使用你的类

修改 `report.py` 程序中的 `read_portfolio()` 函数，使其像练习 4.3 中那样将投资组合读入 `Stock` 实例列表。完成此操作后，修复 `report.py` 和 `pcost.py` 中的所有代码，使其与 `Stock` 实例而非字典一起工作。

提示：你无需对代码进行重大更改。主要是将字典访问（如 `s['shares']`）改为 `s.shares`。

你应该能够像以前一样运行你的函数：

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
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
