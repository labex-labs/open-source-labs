# Analisar a Estrutura da Árvore Binária

O classificador de árvore de decisão possui um atributo chamado `tree_` que permite o acesso a atributos de baixo nível, como `node_count`, o número total de nós, e `max_depth`, a profundidade máxima da árvore. Ele também armazena a estrutura da árvore binária completa, representada como um conjunto de matrizes paralelas. Usando essas matrizes, podemos percorrer a estrutura da árvore para calcular várias propriedades, como a profundidade de cada nó e se ele é ou não uma folha. Abaixo está o código para calcular essas propriedades:

```python
import numpy as np

n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold

node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)
stack = [(0, 0)]  # começa com o ID do nó raiz (0) e sua profundidade (0)
while len(stack) > 0:
    # `pop` garante que cada nó seja visitado apenas uma vez
    node_id, depth = stack.pop()
    node_depth[node_id] = depth

    # Se o filho esquerdo e direito de um nó não forem iguais, temos um nó de divisão
    is_split_node = children_left[node_id] != children_right[node_id]
    # Se um nó de divisão, adicione os filhos esquerdo e direito e a profundidade à `stack`
    # para que possamos percorrer eles
    if is_split_node:
        stack.append((children_left[node_id], depth + 1))
        stack.append((children_right[node_id], depth + 1))
    else:
        is_leaves[node_id] = True

print(
    "A estrutura da árvore binária tem {n} nós e tem a seguinte estrutura da árvore:\n".format(n=n_nodes)
)
for i in range(n_nodes):
    if is_leaves[i]:
        print(
            "{space}nó={node} é um nó folha.".format(
                space=node_depth[i] * "\t", node=i
            )
        )
    else:
        print(
            "{space}nó={node} é um nó de divisão: "
            "vá para o nó {left} se X[:, {feature}] <= {threshold} "
            "senão para o nó {right}.".format(
                space=node_depth[i] * "\t",
                node=i,
                left=children_left[i],
                feature=feature[i],
                threshold=threshold[i],
                right=children_right[i],
            )
        )
```
