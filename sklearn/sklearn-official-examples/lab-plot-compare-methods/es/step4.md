# Estandarización Multidimensional

La Estandarización Multidimensional (MDS) busca una representación de baja dimensión de los datos en la que las distancias respeten adecuadamente las distancias en el espacio de alta dimensión original.

```python
md_scaling = manifold.MDS(
    n_components=n_components,
    max_iter=50,
    n_init=4,
    random_state=0,
    normalized_stress=False,
)
S_scaling = md_scaling.fit_transform(S_points)
```
