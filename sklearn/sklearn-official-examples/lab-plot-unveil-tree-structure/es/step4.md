# Obtener el camino de decisión y los nodos hoja

Podemos obtener el camino de decisión de las muestras de interés utilizando el método `decision_path`. Este método devuelve una matriz de indicadores que nos permite recuperar los nodos por los que atraviesan las muestras de interés. Los ids de las hojas alcanzadas por las muestras de interés se pueden obtener con el método `apply`. Esto devuelve una matriz con los ids de los nodos de las hojas alcanzadas por cada muestra de interés. Utilizando los ids de las hojas y el `decision_path` podemos obtener las condiciones de división que se utilizaron para predecir una muestra o un grupo de muestras. A continuación se muestra el código para obtener el camino de decisión y los nodos hoja para una muestra:

```python
node_indicator = clf.decision_path(X_test)
leaf_id = clf.apply(X_test)

sample_id = 0
# obtener los ids de los nodos por los que pasa `sample_id`, es decir, la fila `sample_id`
node_index = node_indicator.indices[
    node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
]

print("Reglas utilizadas para predecir la muestra {id}:\n".format(id=sample_id))
for node_id in node_index:
    # continuar con el siguiente nodo si es un nodo hoja
    if leaf_id[sample_id] == node_id:
        continue

    # comprobar si el valor de la característica de división para la muestra 0 es menor que el umbral
    if X_test[sample_id, feature[node_id]] <= threshold[node_id]:
        threshold_sign = "<="
    else:
        threshold_sign = ">"

    print(
        "nodo de decisión {node} : (X_test[{sample}, {feature}] = {value}) "
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
