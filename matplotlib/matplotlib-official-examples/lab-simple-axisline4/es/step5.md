# Establecer las etiquetas de los intervalos de la segunda coordenada y

Podemos establecer las etiquetas de los intervalos de la segunda coordenada y utilizando la función `set_xticks` y pasando las ubicaciones y etiquetas de los intervalos como argumentos.

```python
ax2.set_xticks([0.,.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi],
               labels=["$0$", r"$\frac{1}{2}\pi$",
                       r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
```
