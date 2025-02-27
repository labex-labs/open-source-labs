# Definir los componentes de la canalización

Definiremos los componentes de la canalización, incluyendo el PCA, el Estandarizador y la Regresión Logística. Estableceremos la tolerancia en un valor grande para acelerar el ejemplo.

```python
# Define a pipeline to search for the best combination of PCA truncation
# and classifier regularization.
pca = PCA()
# Define a Standard Scaler to normalize inputs
scaler = StandardScaler()

logistic = LogisticRegression(max_iter=10000, tol=0.1)

pipe = Pipeline(steps=[("scaler", scaler), ("pca", pca), ("logistic", logistic)])
```
