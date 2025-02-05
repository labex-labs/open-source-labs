# 导入 Matplotlib 并设置 pgf.texsystem 参数

首先，你需要导入 Matplotlib 库，并将 `pgf.texsystem` 参数设置为 `pdflatex`。此参数允许你使用 LaTeX 来定制图表的字体族。

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
})
```
