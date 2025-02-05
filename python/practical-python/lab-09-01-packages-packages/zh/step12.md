# 练习9.2：创建一个应用程序目录

对于一个应用程序来说，仅仅把所有代码放入一个“包”中通常是不够的。有时候还会有支持文件、文档、脚本以及其他内容。这些文件需要存在于你在上面创建的 `porty/` 目录之外。

创建一个名为 `porty-app` 的新目录。将你在练习9.1中创建的 `porty` 目录移动到该目录中。将 `portfolio.csv` 和 `prices.csv` 测试文件复制到这个目录中。另外创建一个 `README.txt` 文件，写入一些关于你自己的信息。现在你的代码应该如下组织：

    porty-app/
        portfolio.csv
        prices.csv
        README.txt
        porty/
            __init__.py
            fileparse.py
            follow.py
            pcost.py
            portfolio.py
            report.py
            stock.py
            tableformat.py
            ticker.py
            typedproperty.py

要运行你的代码，你需要确保你在顶级目录 `porty-app/` 中工作。例如，在终端中：

```python
$ cd porty-app
$ python3
>>> import porty.report
>>>
```

尝试将你之前的一些脚本作为主程序运行：

```python
$ cd porty-app
$ python3 -m porty.report portfolio.csv prices.csv txt
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84

$
```
