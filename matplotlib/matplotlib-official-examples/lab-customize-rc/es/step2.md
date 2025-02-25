# Personaliza parámetros predeterminados

Para personalizar los parámetros predeterminados para una figura específica, puedes utilizar nuevamente el método `rcParams.update()`. Esta vez, pasarás un diccionario de nombres y valores de parámetros que quieres establecer para esa figura. Aquí te presento un ejemplo que establece algunos parámetros predeterminados para una figura específica:

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
