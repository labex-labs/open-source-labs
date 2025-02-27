# Modelle definieren und trainieren

Wir werden zwei Modelle definieren, Multinomial und One-vs-Rest L1 Logistic Regression, und sie mit unterschiedlicher Anzahl von Epochen trainieren.

```python
models = {
    "ovr": {"name": "One versus Rest", "iters": [1, 2, 3]},
    "multinomial": {"name": "Multinomial", "iters": [1, 2, 5]},
}

for model in models:
    # Fügen Sie initiale Chance-Level-Werte hinzu, um die Grafik zu erstellen
    accuracies = [1 / n_classes]
    times = [0]
    densities = [1]

    model_params = models[model]

    # Kleine Anzahl von Epochen für schnelle Laufzeit
    for this_max_iter in model_params["iters"]:
        print(
            "[model=%s, solver=%s] Anzahl der Epochen: %s"
            % (model_params["name"], solver, this_max_iter)
        )
        lr = LogisticRegression(
            solver=solver,
            multi_class=model,
            penalty="l1",
            max_iter=this_max_iter,
            random_state=42,
        )
        t1 = timeit.default_timer()
        lr.fit(X_train, y_train)
        train_time = timeit.default_timer() - t1

        y_pred = lr.predict(X_test)
        accuracy = np.sum(y_pred == y_test) / y_test.shape[0]
        density = np.mean(lr.coef_!= 0, axis=1) * 100
        accuracies.append(accuracy)
        densities.append(density)
        times.append(train_time)
    models[model]["times"] = times
    models[model]["densities"] = densities
    models[model]["accuracies"] = accuracies
    print("Testgenauigkeit für Modell %s: %.4f" % (model, accuracies[-1]))
    print(
        "%% nicht-nulle Koeffizienten für Modell %s, pro Klasse:\n %s"
        % (model, densities[-1])
    )
    print(
        "Laufzeit (%i Epochen) für Modell %s:%.2f"
        % (model_params["iters"][-1], model, times[-1])
    )
```
