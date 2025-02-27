# Iterar sobre lotes pequeños de ejemplos y actualizar los clasificadores

```python
# Le alimentaremos el clasificador con lotes pequeños de 1000 documentos; esto significa
# que tendremos como máximo 1000 documentos en memoria en cualquier momento.
# Cuanto más pequeño sea el lote de documentos, mayor será el costo relativo
# de los métodos de ajuste parcial.
minibatch_size = 1000

# Crear el data_stream que analiza los archivos SGML de Reuters y itera sobre
# los documentos como un flujo.
minibatch_iterators = iter_minibatches(data_stream, minibatch_size)
total_vect_time = 0.0

# Bucle principal: iterar sobre lotes pequeños de ejemplos
for i, (X_train_text, y_train) in enumerate(minibatch_iterators):
    tick = time.time()
    X_train = vectorizer.transform(X_train_text)
    total_vect_time += time.time() - tick

    for cls_name, cls in partial_fit_classifiers.items():
        tick = time.time()
        # actualizar el estimador con los ejemplos del lote pequeño actual
        cls.partial_fit(X_train, y_train, classes=all_classes)

        # acumular estadísticas de precisión en el test
        cls_stats[cls_name]["total_fit_time"] += time.time() - tick
        cls_stats[cls_name]["n_train"] += X_train.shape[0]
        cls_stats[cls_name]["n_train_pos"] += sum(y_train)
        tick = time.time()
        cls_stats[cls_name]["accuracy"] = cls.score(X_test, y_test)
        cls_stats[cls_name]["prediction_time"] = time.time() - tick
        acc_history = (cls_stats[cls_name]["accuracy"], cls_stats[cls_name]["n_train"])
        cls_stats[cls_name]["accuracy_history"].append(acc_history)
        run_history = (
            cls_stats[cls_name]["accuracy"],
            total_vect_time + cls_stats[cls_name]["total_fit_time"],
        )
        cls_stats[cls_name]["runtime_history"].append(run_history)

        if i % 3 == 0:
            print(progress(cls_name, cls_stats[cls_name]))
    if i % 3 == 0:
        print("\n")
```
