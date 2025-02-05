# 定义字体族

接下来，你需要定义想要在图表中使用的字体族。在本示例中，我们将使用 `cmbright` 字体族。

```python
plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "pgf.preamble": "\n".join([
         r"\usepackage[utf8x]{inputenc}",
         r"\usepackage[T1]{fontenc}",
         r"\usepackage{cmbright}",
    ]),
})
```
