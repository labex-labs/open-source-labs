# Determinar Nós Comuns para um Grupo de Amostras

Para um grupo de amostras, podemos determinar os nós comuns pelos quais as amostras passam usando o método `decision_path` e o método `toarray` para converter a matriz indicadora em um array denso.

```python
sample_ids = [0, 1]
# array booleano indicando os nós pelos quais ambas as amostras passam
common_nodes = node_indicator.toarray()[sample_ids].sum(axis=0) == len(sample_ids)
# obter os IDs dos nós usando a posição no array
common_node_id = np.arange(n_nodes)[common_nodes]

print(
    "\nAs seguintes amostras {samples} compartilham o(s) nó(s) {nodes} na árvore.".format(
        samples=sample_ids, nodes=common_node_id
    )
)
print("Isso representa {prop}% de todos os nós.".format(prop=100 * len(common_node_id) / n_nodes))
```
