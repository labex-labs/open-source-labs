# Personalizando el gráfico

Ahora que hemos creado un gráfico básico, personalicémoslo para que sea más atractivo visualmente. Podemos agregar un título, etiquetas de eje y cambiar el color y el estilo de la línea.

```python
# Add title and axis labels
plt.title('Sin Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Change color and style of line
plt.plot(x, y, color='red', linestyle='dashed')
plt.show()
```
