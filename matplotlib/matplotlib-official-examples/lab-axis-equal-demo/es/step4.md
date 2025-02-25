# Ajustar los límites de la gráfica mientras se mantiene la proporción de aspecto de ejes igual

También podemos ajustar los límites de la gráfica mientras se mantiene la proporción de aspecto de ejes igual.

```python
axs[1, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 0].axis('equal')
axs[1, 0].set(xlim=(-3, 3), ylim=(-3, 3))
axs[1, 0].set_title('still a circle, even after changing limits', fontsize=10)
```

La gráfica resultante mostrará un círculo que sigue siendo proporcional incluso después de cambiar los límites.
