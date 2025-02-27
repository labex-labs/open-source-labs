# Récupérer le chemin de décision et les nœuds terminaux

Nous pouvons récupérer le chemin de décision d'échantillons d'intérêt à l'aide de la méthode `decision_path`. Cette méthode renvoie une matrice d'indicateurs qui nous permet de récupérer les nœuds traversés par les échantillons d'intérêt. Les identifiants des nœuds terminaux atteints par les échantillons d'intérêt peuvent être obtenus avec la méthode `apply`. Cela renvoie un tableau des identifiants des nœuds des nœuds terminaux atteints par chaque échantillon d'intérêt. En utilisant les identifiants des nœuds terminaux et le `decision_path`, nous pouvons obtenir les conditions de division qui ont été utilisées pour prédire un échantillon ou un groupe d'échantillons. Voici le code pour récupérer le chemin de décision et les nœuds terminaux pour un échantillon :

```python
node_indicator = clf.decision_path(X_test)
leaf_id = clf.apply(X_test)

sample_id = 0
# obtenir les identifiants des nœuds que `sample_id` traverse, c'est-à-dire la ligne `sample_id`
node_index = node_indicator.indices[
    node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
]

print("Règles utilisées pour prédire l'échantillon {id}:\n".format(id=sample_id))
for node_id in node_index:
    # passer au nœud suivant s'il s'agit d'un nœud terminal
    if leaf_id[sample_id] == node_id:
        continue

    # vérifier si la valeur de la caractéristique de division pour l'échantillon 0 est inférieure au seuil
    if X_test[sample_id, feature[node_id]] <= threshold[node_id]:
        threshold_sign = "<="
    else:
        threshold_sign = ">"

    print(
        "nœud de décision {node} : (X_test[{sample}, {caractéristique}] = {valeur}) "
        "{inégalité} {seuil})".format(
            node=node_id,
            sample=sample_id,
            caractéristique=feature[node_id],
            valeur=X_test[sample_id, feature[node_id]],
            inégalité=threshold_sign,
            seuil=threshold[node_id],
        )
    )
```
