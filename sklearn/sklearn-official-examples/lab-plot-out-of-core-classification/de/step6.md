# Iteriere über Minibatches von Beispielen und aktualisiere die Klassifizierer

```python
# Wir werden den Klassifizierer mit Minibatches von 1000 Dokumenten versorgen; das bedeutet,
# dass wir zu jedem Zeitpunkt maximal 1000 Dokumente im Speicher haben. Je kleiner die Dokumentenmenge
# pro Batch ist, desto größer ist der relative Aufwand der partielle Anpassungsmethoden.
minibatch_size = 1000

# Erstelle den data_stream, der die Reuters-SGML-Dateien analysiert und über die Dokumente als Stream iteriert.
minibatch_iterators = iter_minibatches(data_stream, minibatch_size)
total_vect_time = 0.0

# Hauptschleife: Iteriere über Minibatches von Beispielen
for i, (X_train_text, y_train) in enumerate(minibatch_iterators):
    tick = time.time()
    X_train = vectorizer.transform(X_train_text)
    total_vect_time += time.time() - tick

    for cls_name, cls in partial_fit_classifiers.items():
        tick = time.time()
        # Aktualisiere den Schätzer mit den Beispielen im aktuellen Minibatch
        cls.partial_fit(X_train, y_train, classes=all_classes)

        # Akkumuliere die Testgenauigkeitsstatistiken
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
