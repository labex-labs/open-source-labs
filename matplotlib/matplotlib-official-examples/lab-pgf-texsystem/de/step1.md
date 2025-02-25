# Matplotlib importieren und den pgf.texsystem-Parameter einstellen

Zunächst musst du die Matplotlib-Bibliothek importieren und den `pgf.texsystem`-Parameter auf `pdflatex` setzen. Dieser Parameter ermöglicht es dir, LaTeX zu verwenden, um die Schriftfamilie deines Plots anzupassen.

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
})
```
