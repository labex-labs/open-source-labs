# Trazar la dependencia parcial de los dos modelos juntos

En este paso, trazaremos las curvas de dependencia parcial de los dos modelos en la misma gráfica.

```python
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
tree_disp.plot(ax=ax1)
ax1.set_title("Decision Tree")
mlp_disp.plot(ax=ax2, line_kw={"color": "red"})
ax2.set_title("Multi-layer Perceptron")
```

Otra forma de comparar las curvas es superponerlas. Aquí, creamos una figura con una fila y dos columnas. Los ejes se pasan a la función `PartialDependenceDisplay.plot` como una lista, lo que dibujará las curvas de dependencia parcial de cada modelo en los mismos ejes. La longitud de la lista de ejes debe ser igual al número de gráficos dibujados.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
tree_disp.plot(ax=[ax1, ax2], line_kw={"label": "Decision Tree"})
mlp_disp.plot(
    ax=[ax1, ax2], line_kw={"label": "Multi-layer Perceptron", "color": "red"}
)
ax1.legend()
ax2.legend()
```

`tree_disp.axes_` es un contenedor de matriz de numpy con los ejes utilizados para dibujar las gráficas de dependencia parcial. Esto se puede pasar a `mlp_disp` para tener el mismo efecto de dibujar las gráficas una encima de la otra. Además, `mlp_disp.figure_` almacena la figura, lo que permite cambiar el tamaño de la figura después de llamar a `plot`. En este caso, `tree_disp.axes_` tiene dos dimensiones, por lo que `plot` solo mostrará la etiqueta y las marcas del eje y en la gráfica más a la izquierda.

```python
tree_disp.plot(line_kw={"label": "Decision Tree"})
mlp_disp.plot(
    line_kw={"label": "Multi-layer Perceptron", "color": "red"}, ax=tree_disp.axes_
)
tree_disp.figure_.set_size_inches(10, 6)
tree_disp.axes_[0, 0].legend()
tree_disp.axes_[0, 1].legend()
plt.show()
```
