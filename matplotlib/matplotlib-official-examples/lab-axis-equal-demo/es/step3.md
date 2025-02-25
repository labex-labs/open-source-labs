# Graficar un círculo con una proporción de aspecto de ejes igual

Para establecer la proporción de aspecto de ejes igual, podemos utilizar la función `axis('equal')`.

```python
axs[0, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 1].axis('equal')
axs[0, 1].set_title('equal, looks like circle', fontsize=10)
```

La gráfica resultante mostrará un círculo que es proporcional y visualmente atractivo.
