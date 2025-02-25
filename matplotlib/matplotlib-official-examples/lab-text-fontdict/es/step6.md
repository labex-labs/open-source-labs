# Personalizar las etiquetas de los ejes

También podemos personalizar las etiquetas de los ejes de nuestro gráfico utilizando el diccionario de fuentes. Estableceremos el parámetro fontdict de las funciones xlabel() e ylabel() en nuestro diccionario de fuentes.

```python
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Voltage (mV)', fontdict=font)
```
