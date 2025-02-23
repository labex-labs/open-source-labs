# Personalizando estilos de flechas y burbujas

La flecha entre `xytext` y el punto de anotación, así como la burbuja que cubre el texto de la anotación, son altamente personalizables. A continuación se presentan algunas opciones de parámetros y su resultado.

```python
fig, ax = plt.subplots(figsize=(8, 5))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=3)

ax.annotate(
    'directa',
    xy=(0, 1), xycoords='data',
    xytext=(-50, 30), textcoords='puntos de desplazamiento',
    arrowprops=dict(arrowstyle="->"))
ax.annotate(
    'arc3,\nrad 0.2',
    xy=(0.5, -1), xycoords='data',
    xytext=(-80, -60), textcoords='puntos de desplazamiento',
    arrowprops=dict(arrowstyle="->",
                    connectionstyle="arc3,rad=.2"))
ax.annotate(
    'arco,\nángulo 50',
    xy=(1., 1), xycoords='data',
    xytext=(-90, 50), textcoords='puntos de desplazamiento',
    arrowprops=dict(arrowstyle="->",
                    connectionstyle="arc,angleA=0,armA=50,rad=10"))
ax.annotate(
    'arco,\n brazos',
    xy=(1.5, -1), xycoords='data',
    xytext=(-80, -60), textcoords='puntos de desplazamiento',
    arrowprops=dict(
        arrowstyle="->",
        connectionstyle="arc,angleA=0,armA=40,angleB=-90,armB=30,rad=7"))
ax.annotate(
    'ángulo,\nángulo 90',
    xy=(2., 1), xycoords='data',
    xytext=(-70, 30), textcoords='puntos de desplazamiento',
    arrowprops=dict(arrowstyle="->",
                    connectionstyle="angle,angleA=0,angleB=90,rad=10"))
ax.annotate(
    'angle3,\nángulo -90',
    xy=(2.5, -1), xycoords='data',
    xytext=(-80, -60), textcoords='puntos de desplazamiento',
    arrowprops=dict(arrowstyle="->",
                    connectionstyle="angle3,angleA=0,angleB=-90"))
ax.annotate(
    'ángulo,\nredondeado',
    xy=(3., 1), xycoords='data',
    xytext=(-60, 30), textcoords='puntos de desplazamiento',
    bbox=dict(boxstyle="round", fc="0.8"),
    arrowprops=dict(arrowstyle="->",
                    connectionstyle="angle,angleA=0,angleB=90,rad=10"))
ax.annotate(
    'ángulo,\nround4',
    xy=(3.5, -1), xycoords='data',
    xytext=(-70, -80), textcoords='puntos de desplazamiento',
    size=20,
    bbox=dict(boxstyle="round4,pad=.5", fc="0.8"),
    arrowprops=dict(arrowstyle="->",
                    connectionstyle="angle,angleA=0,angleB=-90,rad=10"))
ax.annotate(
    'ángulo,\nencogimiento',
    xy=(4., 1), xycoords='data',
    xytext=(-60, 30), textcoords='puntos de desplazamiento',
    bbox=dict(boxstyle="round", fc="0.8"),
    arrowprops=dict(arrowstyle="->",
                    shrinkA=0, shrinkB=10,
                    connectionstyle="angle,angleA=0,angleB=90,rad=10"))
# Puedes pasar una cadena vacía para obtener solo las flechas de anotación renderizadas
ax.annotate('', xy=(4., 1.), xycoords='data',
            xytext=(4.5, -1), textcoords='data',
            arrowprops=dict(arrowstyle="<->",
                            connectionstyle="bar",
                            ec="k",
                            shrinkA=5, shrinkB=5))

ax.set(xlim=(-1, 5), ylim=(-4, 3))
```
