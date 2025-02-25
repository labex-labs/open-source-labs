# Crear un gráfico con escala logit y notación de supervivencia

Crearemos un gráfico con escala logit y notación de supervivencia. Esto se puede hacer configurando la escala del eje y a logit y configurando el parámetro `one_half` a `"1/2"` y el parámetro `use_overline` a `True` usando `set_yscale("logit", one_half="1/2", use_overline=True)`. También graficaremos las funciones de distribución acumulativa para las distribuciones normal, laplaciana y de Cauchy usando `plot()` y agregaremos una leyenda usando `legend()`.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.set_yscale("logit", one_half="1/2", use_overline=True)
axs.set_ylim(1e-5, 1 - 1e-5)
axs.legend()
axs.grid()

plt.show()
```
