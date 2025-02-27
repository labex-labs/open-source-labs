# Entrenar MLPClassifier

Crearemos un MLPClassifier con una sola capa oculta que contiene 40 neuronas. Debido a las restricciones de recursos, entrenaremos el MLP solo durante 8 iteraciones. También capturaremos la advertencia `ConvergenceWarning` que se lanzará porque el modelo no convergerá dentro del número limitado de iteraciones.

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
