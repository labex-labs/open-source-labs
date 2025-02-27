# Entraîner et évaluer l'estimateur

La prochaine étape consiste à entraîner et évaluer l'estimateur en utilisant chacun des critères d'arrêt. Nous utiliserons une boucle pour itérer sur chaque estimateur et critère d'arrêt, et nous utiliserons une autre boucle pour itérer sur différents nombres maximaux d'itérations. Nous stockerons ensuite les résultats dans un DataFrame pandas pour une représentation graphique facile.

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

# Transformer les résultats en un DataFrame pandas pour une représentation graphique facile
columns = [
    "Critère d'arrêt",
    "max_iter",
    "Temps d'ajustement (sec)",
    "n_iter_",
    "Score d'entraînement",
    "Score de test",
]
results_df = pd.DataFrame(results, columns=columns)
```
