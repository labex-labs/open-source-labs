# Personalizar el gráfico

Podemos personalizar el gráfico aún más agregando etiquetas de eje y un título. También podemos cambiar el color de las etiquetas de eje y el título de la leyenda. El siguiente código demuestra cómo personalizar el gráfico:

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply', color='blue')
ax.set_xlabel('fruit names', color='blue')
ax.set_title('Fruit supply by kind and color', color='purple')
ax.legend(title='Fruit color', title_color='red', labelcolor='green')
plt.show()
```
