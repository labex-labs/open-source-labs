# Définir et entraîner les modèles

Nous allons définir deux modèles, la régression logistique multinomiale et la régression logistique L1 One-vs-Rest, et les entraîner avec un nombre différent d'époques.

```python
models = {
    "ovr": {"name": "One versus Rest", "iters": [1, 2, 3]},
    "multinomial": {"name": "Multinomial", "iters": [1, 2, 5]},
}

for model in models:
    # Ajoutez des valeurs initiales de niveau aléatoire pour les fins de tracé
    accuracies = [1 / n_classes]
    times = [0]
    densities = [1]

    model_params = models[model]

    # Petit nombre d'époques pour une exécution rapide
    for this_max_iter in model_params["iters"]:
        print(
            "[model=%s, solver=%s] Nombre d'époques: %s"
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
    print("Précision de test pour le modèle %s: %.4f" % (model, accuracies[-1]))
    print(
        "%% de coefficients non nuls pour le modèle %s, par classe:\n %s"
        % (model, densities[-1])
    )
    print(
        "Temps d'exécution (%i epoques) pour le modèle %s:%.2f"
        % (model_params["iters"][-1], model, times[-1])
    )
```
