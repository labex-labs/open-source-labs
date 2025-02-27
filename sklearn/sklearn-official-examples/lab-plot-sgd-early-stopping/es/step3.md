# Entrenar y evaluar el estimador

El siguiente paso es entrenar y evaluar el estimador utilizando cada criterio de parada. Utilizaremos un bucle para iterar sobre cada estimador y criterio de parada, y utilizaremos otro bucle para iterar sobre diferentes iteraciones máximas. Luego almacenaremos los resultados en un dataframe de pandas para una representación gráfica fácil.

```python
results = []
for estimator_name, estimator in estimator_dict.items():
    print(estimator_name + ": ", end="")
    for max_iter in range(1, 50):
        print(".", end="")
        sys.stdout.flush()

        fit_time, n_iter, train_score, test_score = fit_and_score(
            estimator, max_iter, X_train, X_test, y_train, y_test
        )

        results.append(
            (estimator_name, max_iter, fit_time, n_iter, train_score, test_score)
        )
    print("")

# Transformar los resultados en un dataframe de pandas para una representación gráfica fácil
columns = [
    "Criterio de parada",
    "max_iter",
    "Tiempo de ajuste (seg)",
    "n_iter_",
    "Puntuación de entrenamiento",
    "Puntuación de prueba",
]
results_df = pd.DataFrame(results, columns=columns)
```
