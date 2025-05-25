# Iterar sobre mini-lotes de exemplos e atualizar os classificadores

```python
# Vamos alimentar o classificador com mini-lotes de 1000 documentos; isso significa
# que temos no máximo 1000 documentos na memória em qualquer momento. Quanto menor o
# lote de documentos, maior a sobrecarga relativa dos métodos de ajuste parcial.
minibatch_size = 1000

# Criar o fluxo de dados que analisa arquivos SGML do Reuters e itera sobre
# documentos como um fluxo.
minibatch_iterators = iter_minibatches(data_stream, minibatch_size)
total_vect_time = 0.0

# Loop principal: iterar sobre mini-lotes de exemplos
for i, (X_train_text, y_train) in enumerate(minibatch_iterators):
    tick = time.time()
    X_train = vectorizer.transform(X_train_text)
    total_vect_time += time.time() - tick

    for cls_name, cls in partial_fit_classifiers.items():
        tick = time.time()
        # atualizar o estimador com exemplos no mini-lote atual
        cls.partial_fit(X_train, y_train, classes=all_classes)

        # acumular estatísticas de precisão de teste
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
