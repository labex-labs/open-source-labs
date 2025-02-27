# Definieren der Workflow-Komponenten

Wir definieren die Workflow-Komponenten, einschließlich der PCA, des Standard-Skalierers und der logistischen Regression. Wir setzen die Toleranz auf einen großen Wert, um das Beispiel schneller zu machen.

```python
# Definieren Sie einen Workflow, um die beste Kombination aus PCA-Abschneidung
# und Klassifizierer-Regularisierung zu suchen.
pca = PCA()
# Definieren Sie einen Standard-Skalierer, um die Eingaben zu normalisieren
scaler = StandardScaler()

logistic = LogisticRegression(max_iter=10000, tol=0.1)

pipe = Pipeline(steps=[("scaler", scaler), ("pca", pca), ("logistic", logistic)])
```
