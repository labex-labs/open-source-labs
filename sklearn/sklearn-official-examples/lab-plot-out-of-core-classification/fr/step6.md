# Itérer sur les mini-lots d'exemples et mettre à jour les classifieurs

```python
# Nous alimenterons le classifieur avec des mini-lots de 1000 documents ; cela signifie
# que nous n'avons en mémoire au plus que 1000 documents à tout moment. Plus le lot
# de documents est petit, plus le surcoût relatif des méthodes de mise à jour partielle est élevé.
minibatch_size = 1000

# Créer le flux de données qui analyse les fichiers SGML Reuters et itère sur
# les documents sous forme de flux.
minibatch_iterators = iter_minibatches(data_stream, minibatch_size)
total_vect_time = 0.0

# Boucle principale : itérer sur les mini-lots d'exemples
for i, (X_train_text, y_train) in enumerate(minibatch_iterators):
    tick = time.time()
    X_train = vectorizer.transform(X_train_text)
    total_vect_time += time.time() - tick

    for cls_name, cls in partial_fit_classifiers.items():
        tick = time.time()
        # mettre à jour l'estimateur avec les exemples du mini-batch actuel
        cls.partial_fit(X_train, y_train, classes=all_classes)

        # accumuler les statistiques de précision sur le test
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
