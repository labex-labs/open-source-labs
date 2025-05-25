# Recuperar o Caminho de Decisão e Nós Folha

Podemos recuperar o caminho de decisão de amostras de interesse usando o método `decision_path`. Este método gera uma matriz indicadora que permite recuperar os nós pelos quais as amostras de interesse passam. Os IDs das folhas alcançadas pelas amostras de interesse podem ser obtidos com o método `apply`. Isto retorna um array dos IDs dos nós das folhas alcançadas por cada amostra de interesse. Usando os IDs das folhas e o `decision_path`, podemos obter as condições de divisão usadas para prever uma amostra ou um grupo de amostras. Abaixo está o código para recuperar o caminho de decisão e os nós folha para uma amostra:

```python
node_indicator = clf.decision_path(X_test)
leaf_id = clf.apply(X_test)

sample_id = 0
# obter os IDs dos nós pelos quais a amostra `sample_id` passa, ou seja, a linha `sample_id`
node_index = node_indicator.indices[
    node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
]

print("Regras usadas para prever a amostra {id}:\n".format(id=sample_id))
for node_id in node_index:
    # continuar para o próximo nó se for um nó folha
    if leaf_id[sample_id] == node_id:
        continue

    # verificar se o valor da característica de divisão para a amostra 0 está abaixo do limiar
    if X_test[sample_id, feature[node_id]] <= threshold[node_id]:
        threshold_sign = "<="
    else:
        threshold_sign = ">"

    print(
        "nó de decisão {node} : (X_test[{sample}, {feature}] = {value}) "
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
