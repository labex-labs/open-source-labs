# Analyser la structure de l'arbre binaire

Le classifieur d'arbre de décision possède un attribut appelé `tree_` qui permet d'accéder à des attributs de bas niveau tels que `node_count`, le nombre total de nœuds, et `max_depth`, la profondeur maximale de l'arbre. Il stocke également toute la structure de l'arbre binaire, représentée sous forme de plusieurs tableaux parallèles. En utilisant ces tableaux, nous pouvons parcourir la structure de l'arbre pour calculer diverses propriétés telles que la profondeur de chaque nœud et s'il s'agit ou non d'un nœud terminal. Voici le code pour calculer ces propriétés :

```python
import numpy as np

n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold

node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)
stack = [(0, 0)]  # commencer par l'identifiant du nœud racine (0) et sa profondeur (0)
while len(stack) > 0:
    # `pop` assure que chaque nœud est visité une seule fois
    node_id, depth = stack.pop()
    node_depth[node_id] = depth

    # Si l'enfant gauche et droit d'un nœud sont différents, nous avons un nœud de division
    is_split_node = children_left[node_id]!= children_right[node_id]
    # Si un nœud de division, ajoutez les enfants gauche et droit et la profondeur à `stack`
    # afin que nous puissions parcourir à travers eux
    if is_split_node:
        stack.append((children_left[node_id], depth + 1))
        stack.append((children_right[node_id], depth + 1))
    else:
        is_leaves[node_id] = True

print(
    "La structure de l'arbre binaire a {n} nœuds et a "
    "la structure d'arbre suivante :\n".format(n=n_nodes)
)
for i in range(n_nodes):
    if is_leaves[i]:
        print(
            "{espace}nœud={node} est un nœud terminal.".format(
                espace=node_depth[i] * "\t", node=i
            )
        )
    else:
        print(
            "{espace}nœud={node} est un nœud de division : "
            "aller au nœud {gauche} si X[:, {caractéristique}] <= {seuil} "
            "sinon au nœud {droite}.".format(
                espace=node_depth[i] * "\t",
                node=i,
                gauche=children_left[i],
                caractéristique=feature[i],
                seuil=threshold[i],
                droite=children_right[i],
            )
        )
```
