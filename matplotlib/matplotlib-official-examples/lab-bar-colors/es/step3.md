# Crear el gráfico de barras

Ahora, podemos crear el gráfico de barras utilizando los datos que definimos en el Paso 2. Utilizaremos el método `bar()` del módulo `pyplot` de Matplotlib para crear el gráfico. También pasaremos los parámetros `label` y `color` para controlar las entradas de la leyenda y los colores de las barras, respectivamente. El siguiente código demuestra cómo crear el gráfico de barras:

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')
plt.show()
```
