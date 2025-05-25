# Importar Matplotlib e Definir o Parâmetro pgf.texsystem

Primeiramente, você precisa importar a biblioteca Matplotlib e definir o parâmetro `pgf.texsystem` como `pdflatex`. Este parâmetro permite que você use LaTeX para personalizar a família de fontes do seu gráfico.

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
})
```
