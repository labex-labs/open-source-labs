# Определяем семейство шрифтов

Далее вам нужно определить семейство шрифтов, которое вы хотите использовать в своем графике. В этом примере мы будем использовать семейство шрифтов `cmbright`.

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
