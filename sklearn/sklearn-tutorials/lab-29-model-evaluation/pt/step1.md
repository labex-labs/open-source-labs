# Método de Pontuação do Estimator

O método de pontuação do Estimator é um critério de avaliação padrão fornecido pelo scikit-learn para cada estimador. Ele calcula uma pontuação que representa a qualidade das previsões do modelo. Você pode encontrar mais informações sobre isso na documentação de cada estimador.

Aqui está um exemplo de como usar o método `score` para um estimador:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()
clf.fit(X, y)

score = clf.score(X, y)
print("Pontuação:", score)
```
