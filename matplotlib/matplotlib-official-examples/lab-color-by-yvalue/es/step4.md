# Crear el gráfico

En este paso, crearemos el gráfico utilizando las matrices enmascaradas creadas en el paso anterior. Trazaremos cada matriz enmascarada por separado y utilizaremos un color diferente para cada una.

```python
fig, ax = plt.subplots()
ax.plot(t, smiddle, t, slower, t, supper)
plt.show()
```
