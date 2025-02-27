# Обучение MLPClassifier

Мы создадим классификатор MLPClassifier (Многослойный персептрон) с одним скрытым слоем, содержащим 40 нейронов. Из-за ограничений ресурсов мы обучим MLP только на 8 итерациях. Также мы обработаем предупреждение `ConvergenceWarning`, которое будет выдано, так как модель не сойдется за ограниченное количество итераций.

```python
mlp = MLPClassifier(
    hidden_layer_sizes=(40,),
    max_iter=8,
    alpha=1e-4,
    solver="sgd",
    verbose=10,
    random_state=1,
    learning_rate_init=0.2,
)

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=ConvergenceWarning, module="sklearn")
    mlp.fit(X_train, y_train)
```
