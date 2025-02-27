# Componentes independientes - FastICA

El Análisis de Componentes Independientes (ICA) es un método para separar señales multivariadas en subcomponentes aditivos que son lo más independientes posible. Aplicamos FastICA, que es un algoritmo rápido y robusto para el ICA.

```python
# Componentes independientes - FastICA
ica_estimator = decomposition.FastICA(
    n_components=n_components, max_iter=400, whiten="arbitrary-variance", tol=15e-5
)
ica_estimator.fit(faces_centered)
plot_gallery(
    "Componentes independientes - FastICA", ica_estimator.components_[:n_components]
)
```
