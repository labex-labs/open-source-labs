# Añadir una anotación

Podemos añadir una anotación al gráfico polar especificando la ubicación de la misma. En este caso, elegimos un punto específico del gráfico y lo anotamos.

```python
ind = 800
thisr, thistheta = r[ind], theta[ind]
ax.plot([thistheta], [thisr], 'o')
ax.annotate('una anotación polar',
            xy=(thistheta, thisr),  # theta, radio
            xytext=(0.05, 0.05),    # fracción, fracción
            textcoords='fracción de la figura',
            arrowprops=dict(facecolor='negro', shrink=0.05),
            horizontalalignment='izquierda',
            verticalalignment='abajo',
            )
```
