# Criar Conjuntos de Treino e Teste

Dividimos o conjunto de dados em um conjunto de treino com 1000 amostras e um conjunto de teste com 100 amostras. Adicionamos ruído Gaussiano ao conjunto de teste e criamos duas cópias dos dados originais; uma com ruído e outra sem ruído.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=0, train_size=1_000, test_size=100
)

rng = np.random.RandomState(0)
noise = rng.normal(scale=0.25, size=X_test.shape)
X_test_noisy = X_test + noise

noise = rng.normal(scale=0.25, size=X_train.shape)
X_train_noisy = X_train + noise
```
