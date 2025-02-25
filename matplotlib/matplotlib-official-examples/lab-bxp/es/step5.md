# Activar o desactivar la visualización de diferentes elementos

Podemos activar o desactivar la visualización de diferentes elementos del diagrama de caja utilizando varios parámetros en la función `bxp()`. En este ejemplo, demostramos cómo mostrar o ocultar la media, la caja, las tapas, las muescas y los valores atípicos.

```python
# Toggle the display of different elements
plt.bxp(stats, showmeans=True, showbox=False, showcaps=False, shownotches=True, showfliers=False)
plt.show()
```
