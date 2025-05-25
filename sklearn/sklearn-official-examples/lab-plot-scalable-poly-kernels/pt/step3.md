# Estabelecer o Modelo de Aproximação do Kernel

Agora, treinaremos SVMs lineares em características geradas pelo PolynomialCountSketch com diferentes valores para `n_components`. Usaremos um loop para iterar através de diferentes valores para `n_components` e imprimiremos a precisão de cada modelo.

```python
from sklearn.kernel_approximation import PolynomialCountSketch
from sklearn.pipeline import make_pipeline

n_runs = 1
N_COMPONENTS = [250, 500, 1000, 2000]

for n_components in N_COMPONENTS:
    ps_lsvm_score = 0
    for _ in range(n_runs):
        # Treinar uma SVM linear em características geradas pelo PolynomialCountSketch
        pipeline = make_pipeline(
            PolynomialCountSketch(n_components=n_components, degree=4),
            LinearSVC(dual="auto"),
        )
        pipeline.fit(X_train, y_train)
        ps_lsvm_score += 100 * pipeline.score(X_test, y_test)

    ps_lsvm_score /= n_runs

    # Imprimir a precisão do modelo
    print(f"Precisão da SVM Linear em {n_components} características PolynomialCountSketch: {ps_lsvm_score:.2f}%")
```
