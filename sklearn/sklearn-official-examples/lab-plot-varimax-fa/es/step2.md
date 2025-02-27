# Ejecutar Análisis Factorial con Rotación Varimax

Ahora ejecutaremos el Análisis Factorial en el conjunto de datos Iris con rotación Varimax para descubrir la estructura subyacente de los datos. Compararemos los resultados con el PCA y el Análisis Factorial no rotado.

```python
# Ejecutar análisis factorial con rotación Varimax
n_comps = 2

métodos = [
    ("PCA", PCA()),
    ("Análisis Factorial no rotado", FactorAnalysis()),
    ("Análisis Factorial Varimax", FactorAnalysis(rotation="varimax")),
]
fig, axes = plt.subplots(ncols=len(métodos), figsize=(10, 8), sharey=True)

for ax, (método, fa) in zip(axes, métodos):
    fa.set_params(n_components=n_comps)
    fa.fit(X)

    componentes = fa.components_.T
    print("\n\n %s :\n" % método)
    print(componentes)

    vmax = np.abs(componentes).max()
    ax.imshow(componentes, cmap="RdBu_r", vmax=vmax, vmin=-vmax)
    ax.set_yticks(np.arange(len(nombres_caracteristicas)))
    ax.set_yticklabels(nombres_caracteristicas)
    ax.set_title(str(método))
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Comp. 1", "Comp. 2"])
fig.suptitle("Factores")
plt.tight_layout()
plt.show()
```
