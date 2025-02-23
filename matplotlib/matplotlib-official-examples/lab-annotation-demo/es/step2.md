# Usando múltiples sistemas de coordenadas y tipos de eje

Puedes especificar el `xypoint` y el `xytext` en diferentes posiciones y sistemas de coordenadas, y, opcionalmente, activar una línea de conexión y marcar el punto con un marcador. Las anotaciones también funcionan en ejes polares.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='polar'), figsize=(3, 3))
r = np.arange(0, 1, 0.001)
theta = 2*2*np.pi*r
line, = ax.plot(theta, r)

ind = 800
thisr, thistheta = r[ind], theta[ind]
ax.plot([thistheta], [thisr], 'o')
ax.annotate('una anotación polar',
            xy=(thistheta, thisr),  # theta, radio
            xytext=(0.05, 0.05),    # fracción, fracción
            textcoords='fracción de figura',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom')
```
