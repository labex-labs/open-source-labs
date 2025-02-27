# Das Kernapproximationsmodell etablieren

Wir werden jetzt lineare SVMs auf Merkmalen trainieren, die von PolynomialCountSketch mit unterschiedlichen Werten für n_components generiert werden. Wir verwenden eine Schleife, um durch verschiedene Werte für n_components zu iterieren und die Genauigkeit jedes Modells auszugeben.

```python
from sklearn.kernel_approximation import PolynomialCountSketch

n_runs = 1
N_COMPONENTS = [250, 500, 1000, 2000]

for n_components in N_COMPONENTS:
    ps_lsvm_score = 0
    for _ in range(n_runs):
        # Trainiere eine lineare SVM auf Merkmalen, die von PolynomialCountSketch generiert werden
        pipeline = make_pipeline(
            PolynomialCountSketch(n_components=n_components, degree=4),
            LinearSVC(dual="auto"),
        )
        pipeline.fit(X_train, y_train)
        ps_lsvm_score += 100 * pipeline.score(X_test, y_test)

    ps_lsvm_score /= n_runs

    # Gib die Genauigkeit des Modells aus
    print(f"Linear SVM score on {n_components} PolynomialCountSketch features: {ps_lsvm_score:.2f}%")
```
