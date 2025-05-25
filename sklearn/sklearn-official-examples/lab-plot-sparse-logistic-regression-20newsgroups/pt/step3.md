# Definir e Treinar Modelos

Vamos definir dois modelos, Regressão Logística L1 Multinomial e One-vs-Rest, e treiná-los com diferentes números de épocas.

```python
models = {
    "ovr": {"name": "One versus Rest", "iters": [1, 2, 3]},
    "multinomial": {"name": "Multinomial", "iters": [1, 2, 5]},
}

for model in models:
    # Adicionar valores iniciais de nível de chance para fins de plotagem
    accuracies = [1 / n_classes]
    times = [0]
    densities = [1]

    model_params = models[model]

    # Pequeno número de épocas para tempo de execução rápido
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
        density = np.mean(lr.coef_ != 0, axis=1) * 100
        accuracies.append(accuracy)
        densities.append(density)
        times.append(train_time)
    models[model]["times"] = times
    models[model]["densities"] = densities
    models[model]["accuracies"] = accuracies
    print("Precisão de teste para o modelo %s: %.4f" % (model, accuracies[-1]))
    print(
        "%% de coeficientes não nulos para o modelo %s, por classe:\n %s"
        % (model, densities[-1])
    )
    print(
        "Tempo de execução (%i épocas) para o modelo %s: %.2f"
        % (model_params["iters"][-1], model, times[-1])
    )
```
