# Importar Matplotlib y configurar el parámetro pgf.texsystem

En primer lugar, debe importar la librería Matplotlib y configurar el parámetro `pgf.texsystem` a `pdflatex`. Este parámetro le permite utilizar LaTeX para personalizar la familia de fuentes de su gráfica.

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
})
```
