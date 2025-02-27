# Создание модели приближения ядра

Теперь мы обучим линейные SVM на признаках, сгенерированных с использованием PolynomialCountSketch с разными значениями n_components. Мы будем использовать цикл для перебора различных значений n_components и выводить точность каждой модели.

```python
from sklearn.kernel_approximation import PolynomialCountSketch

n_runs = 1
N_COMPONENTS = [250, 500, 1000, 2000]

for n_components in N_COMPONENTS:
    ps_lsvm_score = 0
    for _ in range(n_runs):
        # Обучаем линейный SVM на признаках, сгенерированных с использованием PolynomialCountSketch
        pipeline = make_pipeline(
            PolynomialCountSketch(n_components=n_components, degree=4),
            LinearSVC(dual="auto"),
        )
        pipeline.fit(X_train, y_train)
        ps_lsvm_score += 100 * pipeline.score(X_test, y_test)

    ps_lsvm_score /= n_runs

    # Выводим точность модели
    print(f"Linear SVM score on {n_components} PolynomialCountSketch features: {ps_lsvm_score:.2f}%")
```
