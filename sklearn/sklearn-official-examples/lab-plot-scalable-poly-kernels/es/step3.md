# Establecer el Modelo de Aproximación del Kernel

Ahora entrenaremos SVMs lineales en las características generadas por PolynomialCountSketch con diferentes valores para n_components. Utilizaremos un bucle para iterar a través de diferentes valores de n_components y mostrar la precisión de cada modelo.

```python
from sklearn.kernel_approximation import PolynomialCountSketch

n_runs = 1
N_COMPONENTS = [250, 500, 1000, 2000]

for n_components in N_COMPONENTS:
    ps_lsvm_score = 0
    for _ in range(n_runs):
        # Entrenar un SVM lineal en las características generadas por PolynomialCountSketch
        pipeline = make_pipeline(
            PolynomialCountSketch(n_components=n_components, degree=4),
            LinearSVC(dual="auto"),
        )
        pipeline.fit(X_train, y_train)
        ps_lsvm_score += 100 * pipeline.score(X_test, y_test)

    ps_lsvm_score /= n_runs

    # Mostrar la precisión del modelo
    print(f"Linear SVM score on {n_components} PolynomialCountSketch features: {ps_lsvm_score:.2f}%")
```
