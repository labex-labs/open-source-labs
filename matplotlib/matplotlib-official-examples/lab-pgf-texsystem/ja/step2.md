# フォントファミリを定義する

次に、プロットで使用したいフォントファミリを定義する必要があります。この例では、`cmbright`フォントファミリを使用します。

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
