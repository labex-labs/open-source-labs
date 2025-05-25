# Definir Matriz de Conectividade

Neste passo, definiremos a matriz de conectividade utilizando a função `grid_to_graph` do scikit-learn. Esta função cria um grafo de conectividade baseado na grade de pixels das imagens.

```python
connectivity = grid_to_graph(*images[0].shape)
```
