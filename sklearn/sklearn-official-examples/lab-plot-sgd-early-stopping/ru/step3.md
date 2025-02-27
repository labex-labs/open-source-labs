# Обучение и оценка оценщика

Следующим шагом является обучение и оценка оценщика с использованием каждого критерия остановки. Мы будем использовать цикл для перебора каждого оценщика и критерия остановки, а также другой цикл для перебора различных максимальных итераций. Затем мы сохраним результаты в pandas dataframe для удобной визуализации.

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

# Преобразование результатов в pandas dataframe для удобной визуализации
columns = [
    "Критерий остановки",
    "max_iter",
    "Время обучения (сек)",
    "n_iter_",
    "Оценка на обучающем наборе",
    "Оценка на тестовом наборе",
]
results_df = pd.DataFrame(results, columns=columns)
```
