# 定义线条样式

在 Matplotlib 中有多种定义线条样式的方法。我们可以使用预定义的样式，如'solid'（实线）、'dashed'（虚线）、'dotted'（点线）和'dashdot'（点划线）。我们也可以使用破折号元组来定义自定义线条样式。

```python
linestyle_str = [
     ('solid','solid'),      # 与 (0, ()) 或'-'相同
     ('dotted', 'dotted'),    # 与 (0, (1, 1)) 或':'相同
     ('dashed', 'dashed'),    # 与'--'相同
     ('dashdot', 'dashdot')]  # 与'-.'相同

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
