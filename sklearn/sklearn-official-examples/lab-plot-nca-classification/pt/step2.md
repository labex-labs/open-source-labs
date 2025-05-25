# Carregar e Preparar os Dados

Em seguida, carregaremos e prepararemos os dados. Carregaremos o conjunto de dados Iris usando o scikit-learn e selecionaremos apenas duas características. Em seguida, dividiremos os dados em um conjunto de treino e um conjunto de teste.

```python
n_neighbors = 1

dataset = datasets.load_iris()
X, y = dataset.data, dataset.target

# apenas duas características são selecionadas. Poderíamos evitar este corte feio usando um conjunto de dados bidimensional
X = X[:, [0, 2]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.7, random_state=42
)
```
