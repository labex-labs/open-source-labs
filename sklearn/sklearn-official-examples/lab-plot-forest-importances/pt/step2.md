# Gerar Dados

Vamos gerar um conjunto de dados sintético com apenas 3 características informativas. Explicitamente, não embaralharemos o conjunto de dados para garantir que as características informativas corresponderão às três primeiras colunas de X. Além disso, dividiremos o nosso conjunto de dados em subconjuntos de treino e teste.

```python
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=3,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    random_state=0,
    shuffle=False,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
```
