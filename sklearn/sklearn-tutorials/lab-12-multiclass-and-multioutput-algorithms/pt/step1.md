# Classificação Multiclasse

#### Descrição do Problema

A classificação multiclasse é uma tarefa de classificação com mais de duas classes. Cada amostra é atribuída a apenas uma classe.

#### Formato do Alvo

Uma representação válida de alvos multiclasse é um vetor unidimensional ou coluna contendo mais de dois valores discretos.

#### Exemplo

Vamos usar o conjunto de dados Iris para demonstrar a classificação multiclasse:

```python
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# Carregar o conjunto de dados Iris
X, y = datasets.load_iris(return_X_y=True)

# Ajustar um modelo de regressão logística usando OneVsRestClassifier
model = OneVsRestClassifier(LogisticRegression())
model.fit(X, y)

# Fazer previsões
predictions = model.predict(X)
print(predictions)
```
