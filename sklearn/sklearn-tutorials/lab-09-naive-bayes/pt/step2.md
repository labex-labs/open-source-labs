# Dividir o Conjunto de Dados em Conjuntos de Treino e Teste

Em seguida, dividiremos o conjunto de dados em conjuntos de treino e teste utilizando a função `train_test_split` do módulo `sklearn.model_selection`. O conjunto de treino será utilizado para treinar o classificador Naive Bayes, e o conjunto de teste será utilizado para avaliar o seu desempenho.

```python
from sklearn.model_selection import train_test_split

# Dividir o conjunto de dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
