# Matplotlib をインポートして pgf.texsystem パラメータを設定する

まず、Matplotlib ライブラリをインポートして、`pgf.texsystem`パラメータを`pdflatex`に設定する必要があります。このパラメータを使うと、LaTeX を使ってプロットのフォントファミリをカスタマイズできます。

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
})
```
