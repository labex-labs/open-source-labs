# Entrenar y probar los clasificadores

Entrenaremos y probaremos cada clasificador para ver cómo se comportan con los datos generados. Repetiremos este proceso varias veces para obtener una puntuación de precisión promedio.

```python
n_train = 20  # muestras para el entrenamiento
n_test = 200  # muestras para la prueba
n_averages = 50  # cuántas veces se repetirá la clasificación
n_features_max = 75  # número máximo de características
step = 4  # tamaño del paso para el cálculo

acc_clf1, acc_clf2, acc_clf3 = [], [], []
n_features_range = range(1, n_features_max + 1, step)

for n_features in n_features_range:
    score_clf1, score_clf2, score_clf3 = 0, 0, 0
    for _ in range(n_averages):
        X, y = generate_data(n_train, n_features)

        clf1.fit(X, y)
        clf2.fit(X, y)
        clf3.fit(X, y)

        X, y = generate_data(n_test, n_features)
        score_clf1 += clf1.score(X, y)
        score_clf2 += clf2.score(X, y)
        score_clf3 += clf3.score(X, y)

    acc_clf1.append(score_clf1 / n_averages)
    acc_clf2.append(score_clf2 / n_averages)
    acc_clf3.append(score_clf3 / n_averages)
```
