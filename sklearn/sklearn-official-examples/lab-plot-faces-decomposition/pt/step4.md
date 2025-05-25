# Componentes Independentes - FastICA

A Análise de Componentes Independentes (ICA) é um método para separar sinais multivariados em subcomponentes aditivos que são maximamente independentes. Aplicamos o FastICA, que é um algoritmo rápido e robusto para ICA.

```python
# Componentes Independentes - FastICA
ica_estimator = decomposition.FastICA(
    n_components=n_components, max_iter=400, whiten="arbitrary-variance", tol=15e-5
)
ica_estimator.fit(faces_centered)
plot_gallery(
    "Componentes Independentes - FastICA", ica_estimator.components_[:n_components]
)
```
