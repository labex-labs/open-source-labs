# 选择默认等宽字体

Matplotlib中的默认等宽字体由操作系统决定。我们可以通过将`font.family`参数设置为`'monospace'`来选择使用默认等宽字体。为此，我们可以使用以下代码：

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
```
