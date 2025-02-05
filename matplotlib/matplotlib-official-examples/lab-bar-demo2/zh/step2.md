# 创建柱状图的数据

在这一步中，我们需要为柱状图创建数据。我们将使用 numpy 库来创建一个值数组，用于绘制柱状图。

```python
from basic_units import cm, inch

cms = cm * np.arange(0, 10, 2)
bottom = 0 * cm
width = 0.8 * cm
```
