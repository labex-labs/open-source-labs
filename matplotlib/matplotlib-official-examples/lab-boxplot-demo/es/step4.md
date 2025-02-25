# Personalizar el diagrama de caja

Podemos personalizar el diagrama de caja cambiando la apariencia de la caja, las bigotes y los valores atípicos. También podemos crear múltiples diagramas de caja en la misma gráfica para comparar diferentes grupos de datos. Aquí hay algunos ejemplos de cómo personalizar el diagrama de caja:

```python
# Crear un diagrama de caja con muesca
plt.boxplot(data, notch=True)
plt.show()

# Cambiar los símbolos de los puntos atípicos a diamantes verdes
plt.boxplot(data, flierprops=dict(marker='D', markerfacecolor='g', markersize=8))
plt.show()

# Crear diagramas de caja horizontales
plt.boxplot(data, vert=False)
plt.show()

# Crear múltiples diagramas de caja en una misma gráfica
data1 = np.random.normal(0, 1, 50)
data2 = np.random.normal(1, 1, 50)
data3 = np.random.normal(2, 1, 50)

plt.boxplot([data1, data2, data3])
plt.show()
```
