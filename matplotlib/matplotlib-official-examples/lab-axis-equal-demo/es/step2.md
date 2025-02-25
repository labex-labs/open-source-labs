# Graficar un círculo con una proporción de aspecto de ejes desigual

Primero graficaremos un círculo con una proporción de aspecto de ejes desigual para demostrar la importancia de establecer proporciones iguales de los ejes.

```python
an = np.linspace(0, 2 * np.pi, 100)
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 0].set_title('not equal, looks like ellipse', fontsize=10)
```

La gráfica resultante mostrará un círculo que parece alargado debido a la proporción desigual de los ejes.
