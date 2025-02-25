# Añadir etiquetas y títulos

Finalmente, podemos añadir etiquetas y títulos a nuestro diagrama de caja para que sea más informativo. Podemos añadir etiquetas a los ejes x e y, así como un título a la gráfica. También podemos cambiar el tamaño y el estilo de fuente de las etiquetas y el título. Aquí hay un ejemplo de cómo añadir etiquetas y títulos:

```python
plt.boxplot([data1, data2, data3])
plt.xlabel('Group')
plt.ylabel('Value')
plt.title('Comparison of Three Groups')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
```
