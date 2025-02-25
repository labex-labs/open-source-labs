# Creando un diagrama de dispersión con múltiples grupos

Podemos crear un diagrama de dispersión con múltiples grupos recorriendo cada grupo y creando un diagrama de dispersión para ese grupo. Especificamos el color, el tamaño y la transparencia de los marcadores para cada grupo utilizando los parámetros `c`, `s` y `alpha`, respectivamente. También establecemos el parámetro `label` con el nombre del grupo, que se utilizará en la leyenda.

```python
fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()
```
