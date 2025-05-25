# Criar um Grafo

Crie um grafo que capture a conectividade local. Um número maior de vizinhos resultará em clusters mais homogêneos, mas com um custo em tempo de processamento. Um número muito grande de vizinhos resulta em tamanhos de clusters mais distribuídos uniformemente, mas pode não impor a estrutura do manifold local dos dados.

```python
knn_graph = kneighbors_graph(X, 30, include_self=False)
```
