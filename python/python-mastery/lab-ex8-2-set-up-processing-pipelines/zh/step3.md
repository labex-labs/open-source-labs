# 继续改进

哦，你可以做得更好。让我们把这个整合到你的表格生成代码中。将程序修改如下：

```python
# ticker.py
...

if __name__ == '__main__':
    from follow import follow
    import csv
    from tableformat import create_formatter, print_table

    formatter = create_formatter('text')

    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ['name','price','change'], formatter)
```

这应该会产生如下输出：

          name      price     change
    ---------- ---------- ----------
             C      53.12      -0.21
           UTX      70.04      -0.19
           AXP      62.86      -0.18
           MMM      85.72      -0.22
           MCD      51.38      -0.03
           WMT      49.85      -0.23
            KO       51.6      -0.07
           AIG      71.39      -0.14
            PG      63.05      -0.02
            HD      37.76      -0.19

哇，这太厉害了！而且相当棒。

**讨论**

学到的一些经验：你可以创建各种生成器函数，并将它们链接在一起，以执行涉及数据流管道的处理。

对于生成器函数，一个不错的思维模型可能是乐高积木。你可以制作一系列小的迭代器模式，并开始以各种方式将它们堆叠在一起。这可能是一种非常强大的编程方式。
