# Crear el gráfico de barras horizontales con ruptura

En este paso, crearemos el gráfico de barras horizontales con ruptura. Utilizaremos el método `broken_barh()` de la clase `Axes` para crear el gráfico. El método `broken_barh()` toma tres argumentos: el primer argumento es una lista de tuplas donde cada tupla representa un segmento de la barra y el primer elemento de la tupla es el punto de inicio del segmento y el segundo elemento es la longitud del segmento; el segundo argumento es la coordenada y de la barra; y el tercer argumento es el color de relleno de la barra.

```python
fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='tab:blue')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax.set_ylim(5, 35)
ax.set_xlim(0, 200)
ax.set_xlabel('seconds since start')
ax.set_yticks([15, 25], labels=['Bill', 'Jim'])
ax.grid(True)
ax.annotate('race interrupted', (61, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

plt.show()
```
