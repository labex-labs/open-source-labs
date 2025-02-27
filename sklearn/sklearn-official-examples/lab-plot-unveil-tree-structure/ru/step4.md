# Получить путь решения и листовые узлы

Мы можем получить путь решения для интересующих нас образцов с использованием метода `decision_path`. Этот метод выводит индикаторную матрицу, которая позволяет нам получить узлы, через которые проходят интересующие нас образцы. Идентификаторы листьев, достигнутые интересующими нас образцами, можно получить с использованием метода `apply`. Это возвращает массив идентификаторов узлов листьев, достигнутых каждым интересующим нас образцом. С использованием идентификаторов листьев и `decision_path` мы можем получить условия разделения, которые были использованы для предсказания одного образца или группы образцов. Ниже приведен код для получения пути решения и листовых узлов для одного образца:

```python
node_indicator = clf.decision_path(X_test)
leaf_id = clf.apply(X_test)

sample_id = 0
# obtain ids of the nodes `sample_id` goes through, i.e., row `sample_id`
node_index = node_indicator.indices[
    node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
]

print("Rules used to predict sample {id}:\n".format(id=sample_id))
for node_id in node_index:
    # continue to the next node if it is a leaf node
    if leaf_id[sample_id] == node_id:
        continue

    # check if value of the split feature for sample 0 is below threshold
    if X_test[sample_id, feature[node_id]] <= threshold[node_id]:
        threshold_sign = "<="
    else:
        threshold_sign = ">"

    print(
        "decision node {node} : (X_test[{sample}, {feature}] = {value}) "
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
