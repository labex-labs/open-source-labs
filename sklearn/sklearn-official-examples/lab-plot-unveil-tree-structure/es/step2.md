# Analizar la estructura del árbol binario

El clasificador de árbol de decisión tiene un atributo llamado `tree_` que permite acceder a atributos de bajo nivel como `node_count`, el número total de nodos, y `max_depth`, la profundidad máxima del árbol. También almacena la estructura completa del árbol binario, representada como una serie de arrays paralelos. Utilizando estos arrays, podemos recorrer la estructura del árbol para calcular propiedades diversas, como la profundidad de cada nodo y si es o no una hoja. A continuación se muestra el código para calcular estas propiedades:

```python
import numpy as np

n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold

node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)
stack = [(0, 0)]  # comienza con el id del nodo raíz (0) y su profundidad (0)
while len(stack) > 0:
    # `pop` asegura que cada nodo solo sea visitado una vez
    node_id, depth = stack.pop()
    node_depth[node_id] = depth

    # Si el hijo izquierdo y derecho de un nodo no son iguales, tenemos un nodo de división
    is_split_node = children_left[node_id]!= children_right[node_id]
    # Si es un nodo de división, agrega los hijos izquierdo y derecho y la profundidad a `stack`
    # para que podamos recorrerlos
    if is_split_node:
        stack.append((children_left[node_id], depth + 1))
        stack.append((children_right[node_id], depth + 1))
    else:
        is_leaves[node_id] = True

print(
    "La estructura del árbol binario tiene {n} nodos y tiene "
    "la siguiente estructura de árbol:\n".format(n=n_nodes)
)
for i in range(n_nodes):
    if is_leaves[i]:
        print(
            "{space}nodo={node} es un nodo hoja.".format(
                space=node_depth[i] * "\t", node=i
            )
        )
    else:
        print(
            "{space}nodo={node} es un nodo de división: "
            "ve al nodo {left} si X[:, {feature}] <= {threshold} "
            "sino al nodo {right}.".format(
                space=node_depth[i] * "\t",
                node=i,
                left=children_left[i],
                feature=feature[i],
                threshold=threshold[i],
                right=children_right[i],
            )
        )
```
