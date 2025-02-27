# Componentes no negativos - NMF

A continuación, aplicamos la Factorización de Matriz No Negativa (NMF), que descompone la matriz de datos en dos matrices no negativas, una que contiene los vectores base y la otra que contiene los coeficientes. Esto da como resultado una representación basada en partes de los datos.

```python
# Componentes no negativos - NMF
nmf_estimator = decomposition.NMF(n_components=n_components, tol=5e-3)
nmf_estimator.fit(faces)  # conjunto de datos no negativo original
plot_gallery("Componentes no negativos - NMF", nmf_estimator.components_[:n_components])
```
