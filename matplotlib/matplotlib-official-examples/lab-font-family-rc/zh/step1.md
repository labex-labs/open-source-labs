# 选择默认无衬线字体

Matplotlib 中的默认字体族是无衬线字体。我们可以通过将`font.family`参数设置为`'sans-serif'`来选择使用默认字体族。为此，我们可以使用以下代码：

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
```
