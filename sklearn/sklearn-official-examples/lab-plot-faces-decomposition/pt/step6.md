# Aprendizagem de Dicionário

A aprendizagem de dicionário é um método para encontrar uma representação esparsa dos dados de entrada como uma combinação de elementos simples, que formam um dicionário. Aplicamos o MiniBatchDictionaryLearning, uma versão mais rápida do DictionaryLearning, mais adequada para conjuntos de dados grandes.

```python
# Aprendizagem de Dicionário
batch_dict_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components, alpha=0.1, max_iter=50, batch_size=3, random_state=rng
)
batch_dict_estimator.fit(faces_centered)
plot_gallery("Aprendizagem de Dicionário", batch_dict_estimator.components_[:n_components])
```
