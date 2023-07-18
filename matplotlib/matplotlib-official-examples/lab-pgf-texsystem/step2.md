# Define the Font Family

Next, you need to define the font family that you want to use in your plot. In this example, we will use the `cmbright` font family.

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
