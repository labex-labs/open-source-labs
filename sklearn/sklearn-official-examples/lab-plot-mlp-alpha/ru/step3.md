# Создание классификаторов

Для каждого значения alpha мы создадим классификаторы MLP. Создадим конвейер, который включает в себя StandardScaler для стандартизации данных и MLPClassifier с разными значениями alpha. Зададим решатель 'lbfgs', который является оптимизатором из семейства методов квази-Ньютона. Зададим max_iter равным 2000 и early_stopping равным True, чтобы предотвратить переобучение. Используем два скрытых слоя по 10 нейронов каждый.

```python
classifiers = []
names = []
for alpha in alphas:
    classifiers.append(
        make_pipeline(
            StandardScaler(),
            MLPClassifier(
                solver="lbfgs",
                alpha=alpha,
                random_state=1,
                max_iter=2000,
                early_stopping=True,
                hidden_layer_sizes=[10, 10],
            ),
        )
    )
    names.append(f"alpha {alpha:.2f}")
```
