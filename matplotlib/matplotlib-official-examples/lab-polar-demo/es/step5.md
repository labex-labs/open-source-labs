# Personalizar el gráfico

Para personalizar el gráfico, podemos utilizar los siguientes métodos:

- `set_rmax` para establecer el valor máximo de `r`
- `set_rticks` para establecer los valores de las marcas de graduación de `r`
- `set_rlabel_position` para establecer la posición de las etiquetas radiales

```python
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.set_rlabel_position(-22.5)
```

También podemos agregar un título al gráfico utilizando el método `set_title`.

```python
ax.set_title("A line plot on a polar axis", va='bottom')
```

Finalmente, podemos agregar una cuadrícula al gráfico utilizando el método `grid`.

```python
ax.grid(True)
```
