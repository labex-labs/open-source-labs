# Escolher um Limiar para Agrupar Características em Clusters

Visualmente, escolhemos manualmente um limiar no dendrograma para agrupar as nossas características em clusters e selecionar uma característica de cada cluster para manter, selecionando essas características do nosso conjunto de dados e treinando uma nova floresta aleatória. A precisão de teste da nova floresta aleatória não mudou muito em comparação com a floresta aleatória treinada no conjunto de dados completo.

```python
cluster_ids = hierarchy.fcluster(dist_linkage, 1, criterion="distance")
cluster_id_to_feature_ids = defaultdict(list)
for idx, cluster_id in enumerate(cluster_ids):
    cluster_id_to_feature_ids[cluster_id].append(idx)
selected_features = [v[0] for v in cluster_id_to_feature_ids.values()]

X_train_sel = X_train[:, selected_features]
X_test_sel = X_test[:, selected_features]

clf_sel = RandomForestClassifier(n_estimators=100, random_state=42)
clf_sel.fit(X_train_sel, y_train)
print(
    "Precisão nos dados de teste com características removidas: {:.2f}".format(
        clf_sel.score(X_test_sel, y_test)
    )
)
```
