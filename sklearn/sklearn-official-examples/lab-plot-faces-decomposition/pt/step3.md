# Componentes Não-Negativos - NMF

Em seguida, aplicamos a Fatoração de Matriz Não-Negativa (NMF), que fatoriza a matriz de dados em duas matrizes não-negativas, uma contendo os vetores base e a outra contendo os coeficientes. Isso resulta em uma representação baseada em partes dos dados.

```python
# Componentes Não-Negativos - NMF
nmf_estimator = decomposition.NMF(n_components=n_components, tol=5e-3)
nmf_estimator.fit(faces)  # conjunto de dados original não-negativo
plot_gallery("Componentes Não-Negativos - NMF", nmf_estimator.components_[:n_components])
```
