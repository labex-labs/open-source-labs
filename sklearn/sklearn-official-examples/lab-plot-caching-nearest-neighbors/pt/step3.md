# Calcular o Grafo dos Vizinhos Mais Próximos

Neste passo, calcularemos o grafo dos vizinhos mais próximos utilizando o `KNeighborsTransformer`.

```python
# O transformador calcula o grafo dos vizinhos mais próximos utilizando o número máximo de vizinhos necessário na busca em grade. O modelo classificador filtra o grafo dos vizinhos mais próximos conforme necessário pelo seu próprio parâmetro n_neighbors.
graph_model = KNeighborsTransformer(n_neighbors=max(n_neighbors_list), mode="distance")
```
