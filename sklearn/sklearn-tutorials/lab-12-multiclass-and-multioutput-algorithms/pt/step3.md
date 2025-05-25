# Classificação Multiclasse-Multisaída

#### Descrição do Problema

A classificação multiclasse-multisaída, também conhecida como classificação multitarefa, prevê múltiplas propriedades não binárias para cada amostra. Cada propriedade pode ter mais de duas classes.

#### Formato do Alvo

Uma representação válida de alvos multiclasse-multisaída é uma matriz densa, onde cada linha representa uma amostra e cada coluna representa uma propriedade ou classe diferente.

#### Exemplo

Vamos criar um problema de classificação multiclasse-multisaída usando a função `make_classification`:

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC

# Gerar um problema de classificação multiclasse-multisaída
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_classes=3, random_state=0)

# Ajustar um classificador de vetores de suporte multisaída
model = MultiOutputClassifier(SVC())
model.fit(X, y)

# Fazer previsões
predictions = model.predict(X)
print(predictions)
```
