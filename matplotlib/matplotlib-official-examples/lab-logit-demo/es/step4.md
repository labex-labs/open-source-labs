# Crear un gráfico con escala lineal

Crearemos un gráfico con escala lineal. Esto se puede hacer simplemente graficando las funciones de distribución acumulativa para las distribuciones normal, laplaciana y de Cauchy usando `plot()` y agregando una leyenda usando `legend()`.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.legend()
axs.grid()

plt.show()
```
