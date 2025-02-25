# 線スタイルを定義する

Matplotlibで線スタイルを定義する方法はいくつかあります。'solid'（実線）、'dashed'（破線）、'dotted'（点線）、'dashdot'（一点鎖線）などの事前定義済みのスタイルを使用できます。また、ダッシュタプルを使ってカスタムの線スタイルを定義することもできます。

```python
linestyle_str = [
     ('solid', 'solid'),      # (0, ()) または '-' と同じ
     ('dotted', 'dotted'),    # (0, (1, 1)) または ':' と同じ
     ('dashed', 'dashed'),    # '--' と同じ
     ('dashdot', 'dashdot')]  # '-.' と同じ

linestyle_tuple = [
     ('loosely dotted',        (0, (1, 10))),
     ('dotted',                (0, (1, 1))),
     ('densely dotted',        (0, (1, 1))),
     ('long dash with offset', (5, (10, 3))),
     ('loosely dashed',        (0, (5, 10))),
     ('dashed',                (0, (5, 5))),
     ('densely dashed',        (0, (5, 1))),

     ('loosely dashdotted',    (0, (3, 10, 1, 10))),
     ('dashdotted',            (0, (3, 5, 1, 5))),
     ('densely dashdotted',    (0, (3, 1, 1, 1))),

     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]
```
