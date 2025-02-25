# Líneas de corriente sin interrupciones

En este paso, crearemos un gráfico de flujo con líneas de corriente sin interrupciones. El parámetro `broken_streamlines` controla si las líneas de corriente deben romperse cuando exceden el límite de líneas dentro de una sola celda de cuadrícula.

```python
plt.streamplot(X, Y, U, V, broken_streamlines=False)
plt.title('Streamplot with Unbroken Streamlines')
plt.show()
```
