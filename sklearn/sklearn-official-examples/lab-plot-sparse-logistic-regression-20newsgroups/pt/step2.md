# Carregar e Preparar os Dados

Em seguida, carregamos o conjunto de dados `20newsgroups` e preparamos os dados para treino e teste.

```python
# Usamos o solucionador SAGA
solver = "saga"

# Reduzimos para um tempo de execução mais rápido
n_samples = 5000

X, y = fetch_20newsgroups_vectorized(subset="all", return_X_y=True)
X = X[:n_samples]
y = y[:n_samples]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, stratify=y, test_size=0.1
)
train_samples, n_features = X_train.shape
n_classes = np.unique(y).shape[0]

print(
    "Conjunto de dados 20newsgroups, train_samples=%i, n_features=%i, n_classes=%i"
    % (train_samples, n_features, n_classes)
)
```
