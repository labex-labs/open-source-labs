# Configurar la gráfica

Ahora, podemos configurar la gráfica. Utilizaremos `plt.subplots()` para crear un objeto de figura y eje. Luego, utilizaremos `ax.triplot()` para trazar la triangulación.

```python
fig, ax = plt.subplots()
ax.triplot(triang)
```
