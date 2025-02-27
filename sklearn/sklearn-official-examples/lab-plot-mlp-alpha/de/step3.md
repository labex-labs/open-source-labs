# Erstelle Klassifizierer

Wir werden für jeden Wert von alpha MLP-Klassifizierer erstellen. Wir werden eine Pipeline erstellen, die StandardScaler enthält, um die Daten zu standardisieren, und MLPClassifier mit unterschiedlichen Werten von alpha. Wir werden den Solver auf 'lbfgs' setzen, was ein Optimierer in der Familie der quasi-Newton-Methoden ist. Wir werden max_iter auf 2000 und early_stopping auf True setzen, um das Overfitting zu vermeiden. Wir werden zwei versteckte Schichten mit jeweils 10 Neuronen verwenden.

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
