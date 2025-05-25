# Classificação Multirótulo

#### Descrição do Problema

A classificação multirótulo é uma tarefa de classificação em que cada amostra pode ser atribuída a múltiplos rótulos. O número de rótulos que cada amostra pode ter é superior a dois.

#### Formato do Alvo

Uma representação válida de alvos multirótulo é uma matriz binária, onde cada linha representa uma amostra e cada coluna representa uma classe. Um valor de 1 indica a presença do rótulo na amostra, enquanto 0 ou -1 indica a ausência.

#### Exemplo

Vamos criar um problema de classificação multirótulo usando a função `make_classification`:

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier

# Gerar um problema de classificação multirótulo
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, random_state=0)
y = y.reshape(-1, 1)

# Ajustar um classificador multisaída de floresta aleatória
model = MultiOutputClassifier(RandomForestClassifier())
model.fit(X, y)

# Fazer previsões
predictions = model.predict(X)
print(predictions)
```
