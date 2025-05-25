# Dividir o Conjunto de Dados

Antes de treinar o classificador de Árvore de Decisão, precisamos dividir o conjunto de dados em conjuntos de treinamento e teste. Usaremos 70% dos dados para treinamento e 30% para teste.

```python
# Dividir o conjunto de dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```
