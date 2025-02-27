# Analysiere die Struktur des binären Baums

Der Entscheidungsbaum-Klassifizierer hat ein Attribut namens `tree_`, das den Zugang zu niedriger Ebene-Attributen wie `node_count`, der Gesamtzahl der Knoten, und `max_depth`, der maximalen Tiefe des Baums, ermöglicht. Es speichert auch die gesamte binäre Baumstruktur, dargestellt als eine Anzahl paralleler Arrays. Mit diesen Arrays können wir die Baumstruktur durchlaufen, um verschiedene Eigenschaften wie die Tiefe jedes Knotens und ob er ein Blatt ist, zu berechnen. Folgender Code berechnet diese Eigenschaften:

```python
import numpy as np

n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold

node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)
stack = [(0, 0)]  # starte mit der Wurzelknoten-ID (0) und ihrer Tiefe (0)
while len(stack) > 0:
    # `pop` stellt sicher, dass jeder Knoten nur einmal besucht wird
    node_id, depth = stack.pop()
    node_depth[node_id] = depth

    # Wenn das linke und rechte Kind eines Knotens nicht gleich ist, haben wir
    # einen Split-Knoten
    is_split_node = children_left[node_id]!= children_right[node_id]
    # Wenn es sich um einen Split-Knoten handelt, füge linkes und rechtes
    # Kind und Tiefe zur `stack` hinzu, damit wir durch sie iterieren können
    if is_split_node:
        stack.append((children_left[node_id], depth + 1))
        stack.append((children_right[node_id], depth + 1))
    else:
        is_leaves[node_id] = True

print(
    "Die binäre Baumstruktur hat {n} Knoten und hat die "
    "folgende Baumstruktur:\n".format(n=n_nodes)
)
for i in range(n_nodes):
    if is_leaves[i]:
        print(
            "{space}node={node} ist ein Blattknoten.".format(
                space=node_depth[i] * "\t", node=i
            )
        )
    else:
        print(
            "{space}node={node} ist ein Split-Knoten: "
            "gehen Sie zu Knoten {left}, wenn X[:, {feature}] <= {threshold} "
            "sonst zu Knoten {right}.".format(
                space=node_depth[i] * "\t",
                node=i,
                left=children_left[i],
                feature=feature[i],
                threshold=threshold[i],
                right=children_right[i],
            )
        )
```
