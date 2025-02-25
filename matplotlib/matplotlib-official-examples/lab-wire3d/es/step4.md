# Personalizar el gráfico

Podemos personalizar el gráfico para que sea más atractivo visualmente. En este ejemplo, agregaremos un título, etiquetas de eje y cambiaremos el color del gráfico.

```python
# Customize the plot
ax.set_title('Gráfico de Contorno')
ax.set_xlabel('Etiqueta de X')
ax.set_ylabel('Etiqueta de Y')
ax.set_zlabel('Etiqueta de Z')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, color='verde')
```
