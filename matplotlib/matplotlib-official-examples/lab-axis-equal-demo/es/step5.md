# Ajustar automáticamente los límites de datos para una proporción de aspecto de ejes igual

También podemos utilizar la función `set_aspect('equal', 'box')` para ajustar automáticamente los límites de datos para una proporción de aspecto de ejes igual.

```python
axs[1, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 1].set_aspect('equal', 'box')
axs[1, 1].set_title('still a circle, auto-adjusted data limits', fontsize=10)
```

La gráfica resultante mostrará un círculo que sigue siendo proporcional y visualmente atractivo.
