# Определяем компоненты конвейера

Мы определим компоненты конвейера, включая PCA, Standard Scaler и логистическую регрессию. Мы установим значение допуска на большое значение, чтобы сделать пример быстрее.

```python
# Define a pipeline to search for the best combination of PCA truncation
# and classifier regularization.
pca = PCA()
# Define a Standard Scaler to normalize inputs
scaler = StandardScaler()

logistic = LogisticRegression(max_iter=10000, tol=0.1)

pipe = Pipeline(steps=[("scaler", scaler), ("pca", pca), ("logistic", logistic)])
```
