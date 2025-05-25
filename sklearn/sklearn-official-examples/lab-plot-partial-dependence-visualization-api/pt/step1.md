# Treinar Modelos no Conjunto de Dados de Diabetes

Neste passo, treinaremos uma árvore de decisão e um perceptron multicamadas no conjunto de dados de diabetes.

```python
diabetes = load_diabetes()
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = diabetes.target

tree = DecisionTreeRegressor()
mlp = make_pipeline(
    StandardScaler(),
    MLPRegressor(hidden_layer_sizes=(100, 100), tol=1e-2, max_iter=500, random_state=0),
)
tree.fit(X, y)
mlp.fit(X, y)
```
