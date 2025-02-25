# Personalizando el gráfico

Podemos personalizar la apariencia de nuestro gráfico agregando etiquetas al eje x y al eje y, y estableciendo la escala del eje y en logarítmica.

```python
ax.set_xticks(x + dimw / 2, labels=map(str, x))
ax.set_yscale('log')

ax.set_xlabel('x')
ax.set_ylabel('y')
```
