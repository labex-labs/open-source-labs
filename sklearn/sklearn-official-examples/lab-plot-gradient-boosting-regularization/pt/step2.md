# Carregar e Dividir Dados

Usaremos o conjunto de dados `make_hastie_10_2` e o dividiremos em conjuntos de treino e teste.

```python
X, y = datasets.make_hastie_10_2(n_samples=4000, random_state=1)

# mapear rótulos de {-1, 1} para {0, 1}
labels, y = np.unique(y, return_inverse=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=0)
```
