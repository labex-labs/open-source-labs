# Carregar e pré-processar os dados

Em seguida, carregaremos o conjunto de dados iris e o pré-processaremos escalando as características usando StandardScaler.

```python
# Carregar o conjunto de dados iris
iris = load_iris()
X, y = iris.data, iris.target

# Escalar as características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```
