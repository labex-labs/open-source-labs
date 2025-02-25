# Matplotlibをインポートしてpgf.texsystemパラメータを設定する

まず、Matplotlibライブラリをインポートして、`pgf.texsystem`パラメータを`pdflatex`に設定する必要があります。このパラメータを使うと、LaTeXを使ってプロットのフォントファミリをカスタマイズできます。

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
})
```
