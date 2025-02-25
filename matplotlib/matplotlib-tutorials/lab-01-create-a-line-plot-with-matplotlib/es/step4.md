# Personalizar el gráfico

Podemos personalizar el gráfico agregando etiquetas a los ejes x e y, un título al gráfico y una leyenda. También podemos cambiar el estilo y el color de la línea.

```python
plt.plot(x, y, linestyle='--', color='red', label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot')
plt.legend()
```
