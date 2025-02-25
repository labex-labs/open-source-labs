# Définir la famille de polices

Ensuite, vous devez définir la famille de polices que vous souhaitez utiliser dans votre graphique. Dans cet exemple, nous utiliserons la famille de polices `cmbright`.

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
