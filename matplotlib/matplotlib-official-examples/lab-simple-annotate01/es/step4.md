# Agregar una anotación de flecha

Ahora agregaremos una anotación de flecha al gráfico. El siguiente código agregará una flecha desde el primer punto de datos hasta el segundo punto de datos.

```python
ax.annotate("", xy=(1, 3), xytext=(2, 4),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
```
