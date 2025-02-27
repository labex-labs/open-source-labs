# Definir y entrenar los modelos

Definiremos dos modelos, Regresión Logística Multinomial y Regresión Logística L1 Uno contra el Resto, y los entrenaremos con un número diferente de épocas.

```python
models = {
    "ovr": {"name": "One versus Rest", "iters": [1, 2, 3]},
    "multinomial": {"name": "Multinomial", "iters": [1, 2, 5]},
}

for model in models:
    # Agregar valores iniciales de nivel de azar para fines de trazado
    accuracies = [1 / n_classes]
    times = [0]
    densities = [1]

    model_params = models[model]

    # Número pequeño de épocas para un tiempo de ejecución rápido
    for this_max_iter in model_params["iters"]:
        print(
            "[model=%s, solver=%s] Número de épocas: %s"
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
    print("Precisión de prueba para el modelo %s: %.4f" % (model, accuracies[-1]))
    print(
        "%% de coeficientes no nulos para el modelo %s, por clase:\n %s"
        % (model, densities[-1])
    )
    print(
        "Tiempo de ejecución (%i épocas) para el modelo %s:%.2f"
        % (model_params["iters"][-1], model, times[-1])
    )
```
