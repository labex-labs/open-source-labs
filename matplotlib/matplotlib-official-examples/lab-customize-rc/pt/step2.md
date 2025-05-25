# Personalizar Parâmetros Padrão

Para personalizar os parâmetros padrão para uma figura específica, você pode usar o método `rcParams.update()` novamente. Desta vez, você passará um dicionário de nomes e valores de parâmetros que deseja definir para essa figura. Aqui está um exemplo que define alguns parâmetros padrão para uma figura específica:

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.weight": "bold",
    "xtick.major.size": 5,
    "xtick.major.pad": 7,
    "xtick.labelsize": 15,
    "grid.color": "0.5",
    "grid.linestyle": "-",
    "grid.linewidth": 5,
    "lines.linewidth": 2,
    "lines.color": "g",
})
```
