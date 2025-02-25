# Die Schriftfamilie definieren

Als nächstes musst du die Schriftfamilie definieren, die du in deinem Plot verwenden möchtest. In diesem Beispiel werden wir die Schriftfamilie `cmbright` verwenden.

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
