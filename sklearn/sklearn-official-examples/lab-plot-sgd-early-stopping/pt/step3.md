# Treinar e avaliar o estimador

O próximo passo é treinar e avaliar o estimador usando cada critério de parada. Usaremos um loop para iterar sobre cada estimador e critério de parada, e usaremos outro loop para iterar sobre diferentes iterações máximas. Em seguida, armazenaremos os resultados em um DataFrame pandas para facilitar o plotagem.

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

# Transformar os resultados em um DataFrame pandas para facilitar a plotagem
columns = [
    "Critério de parada",
    "max_iter",
    "Tempo de ajuste (seg)",
    "n_iter_",
    "Pontuação de treinamento",
    "Pontuação de teste",
]
results_df = pd.DataFrame(results, columns=columns)
```
