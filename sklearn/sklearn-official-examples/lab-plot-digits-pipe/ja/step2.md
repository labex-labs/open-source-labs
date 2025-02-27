# パイプラインコンポーネントを定義する

PCA、Standard Scaler、ロジスティック回帰を含むパイプラインコンポーネントを定義します。例を高速化するために許容誤差を大きな値に設定します。

```python
# Define a pipeline to search for the best combination of PCA truncation
# and classifier regularization.
pca = PCA()
# Define a Standard Scaler to normalize inputs
scaler = StandardScaler()

logistic = LogisticRegression(max_iter=10000, tol=0.1)

pipe = Pipeline(steps=[("scaler", scaler), ("pca", pca), ("logistic", logistic)])
```
