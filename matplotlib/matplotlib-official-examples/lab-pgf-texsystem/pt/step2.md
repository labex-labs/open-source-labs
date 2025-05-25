# Definir a Família de Fontes

Em seguida, você precisa definir a família de fontes que deseja usar em seu gráfico. Neste exemplo, usaremos a família de fontes `cmbright`.

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
