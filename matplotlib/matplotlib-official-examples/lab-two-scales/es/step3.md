# Crear el gráfico

Ahora que tenemos nuestros datos, podemos crear nuestro gráfico. Empezaremos creando un objeto de ejes usando `matplotlib.pyplot.subplots()`. Luego graficaremos nuestro primer conjunto de datos en este objeto de ejes y pondremos el color de la etiqueta en rojo.

```python
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('tiempo (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
```

A continuación, instanciaremos un segundo objeto de ejes que comparta el mismo eje x que el primer objeto de ejes usando el método `ax1.twinx()`. Luego graficaremos nuestro segundo conjunto de datos en este nuevo objeto de ejes y pondremos el color de la etiqueta en azul.

```python
ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)
```

Finalmente, ajustaremos el diseño de nuestro gráfico usando el método `fig.tight_layout()` y lo mostraremos usando `matplotlib.pyplot.show()`.

```python
fig.tight_layout()
plt.show()
```
