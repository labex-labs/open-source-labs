# Definição dos Componentes do Pipeline

Definiremos os componentes do pipeline, incluindo o PCA, o Standard Scaler e a Regressão Logística. Definiremos a tolerância para um valor elevado para acelerar o exemplo.

```python
# Define um pipeline para procurar a melhor combinação de truncamento do PCA
# e regularização do classificador.
pca = PCA()
# Define um Standard Scaler para normalizar as entradas
scaler = StandardScaler()

logistic = LogisticRegression(max_iter=10000, tol=0.1)

pipe = Pipeline(steps=[("scaler", scaler), ("pca", pca), ("logistic", logistic)])
```
