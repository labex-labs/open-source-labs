# Armazenar em Cache o Grafo dos Vizinhos Mais Próximos

Neste passo, armazenaremos em cache o grafo dos vizinhos mais próximos entre múltiplas execuções do `KNeighborsClassifier` utilizando a propriedade de armazenamento em cache de pipelines.

```python
# Observe que fornecemos um diretório para `memory` para armazenar em cache o cálculo do grafo, que será usado várias vezes ao ajustar os hiperparâmetros do classificador.
with TemporaryDirectory(prefix="sklearn_graph_cache_") as tmpdir:
    full_model = Pipeline(
        steps=[("graph", graph_model), ("classifier", classifier_model)], memory=tmpdir
    )
```
