# Entscheidungsweg und Blattknoten abrufen

Wir können den Entscheidungsweg von interessierenden Proben mit der `decision_path`-Methode abrufen. Diese Methode gibt eine Indikatormatrix aus, die uns ermöglicht, die Knoten zu ermitteln, durch die die interessierenden Proben gehen. Die Blatt-IDs, die von interessierenden Proben erreicht werden, können mit der `apply`-Methode erhalten werden. Dies gibt ein Array der Knoten-IDs der Blätter zurück, die von jeder interessierenden Probe erreicht werden. Mit den Blatt-IDs und der `decision_path` können wir die Aufteilungsbedingungen ermitteln, die zur Vorhersage einer Probe oder einer Gruppe von Proben verwendet wurden. Folgender Code ruft den Entscheidungsweg und die Blattknoten für eine Probe ab:

```python
node_indicator = clf.decision_path(X_test)
leaf_id = clf.apply(X_test)

sample_id = 0
# erhalte IDs der Knoten, durch die `sample_id` geht, d.h., Zeile `sample_id`
node_index = node_indicator.indices[
    node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
]

print("Regeln, die zur Vorhersage von Probe {id} verwendet werden:\n".format(id=sample_id))
for node_id in node_index:
    # gehe zum nächsten Knoten, wenn es ein Blattknoten ist
    if leaf_id[sample_id] == node_id:
        continue

    # überprüfe, ob der Wert der aufgeteilten Eigenschaft für Probe 0 unter der Schwelle liegt
    if X_test[sample_id, feature[node_id]] <= threshold[node_id]:
        threshold_sign = "<="
    else:
        threshold_sign = ">"

    print(
        "Entscheidungsknoten {node} : (X_test[{sample}, {feature}] = {value}) "
        "{inequality} {threshold})".format(
            node=node_id,
            sample=sample_id,
            feature=feature[node_id],
            value=X_test[sample_id, feature[node_id]],
            inequality=threshold_sign,
            threshold=threshold[node_id],
        )
    )
```
