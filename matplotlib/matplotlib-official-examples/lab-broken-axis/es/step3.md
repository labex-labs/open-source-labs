# Crear las Subfiguras

A continuación, crearemos dos subfiguras (subplots) - una para los valores atípicos (outliers) y otra para la mayoría de los datos. Usaremos `plt.subplots` para crear las subfiguras y estableceremos el parámetro `sharex` en `True` para que compartan el mismo eje x.

```python
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
```
