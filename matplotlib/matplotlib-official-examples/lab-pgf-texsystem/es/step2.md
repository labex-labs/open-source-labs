# Definir la familia de fuentes

A continuación, debe definir la familia de fuentes que desea utilizar en su gráfica. En este ejemplo, usaremos la familia de fuentes `cmbright`.

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
