# Trainiere und bewerte den Schätzer

Der nächste Schritt besteht darin, den Schätzer unter Verwendung jedes Stoppkriteriums zu trainieren und zu bewerten. Wir werden eine Schleife verwenden, um über jeden Schätzer und jedes Stoppkriterium zu iterieren, und wir werden eine weitere Schleife verwenden, um über verschiedene maximale Iterationen zu iterieren. Anschließend werden wir die Ergebnisse in einem pandas-DataFrame speichern, um eine einfache Visualisierung zu ermöglichen.

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

# Transformiere die Ergebnisse in einen pandas-DataFrame für eine einfache Visualisierung
columns = [
    "Stoppkriterium",
    "max_iter",
    "Fit-Zeit (sec)",
    "n_iter_",
    "Trainingsscore",
    "Testscore",
]
results_df = pd.DataFrame(results, columns=columns)
```
