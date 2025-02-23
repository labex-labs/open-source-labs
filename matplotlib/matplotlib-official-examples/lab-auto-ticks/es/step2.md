# Diagrama de dispersión con el modo de autolimitación round_numbers

En este paso, cambiaremos el `axes.autolimit_mode` a 'round_numbers' y crearemos un diagrama de dispersión para mantener las marcas de graduación en números redondeados y también tener marcas de graduación en los bordes.

```python
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
plt.show()
```
