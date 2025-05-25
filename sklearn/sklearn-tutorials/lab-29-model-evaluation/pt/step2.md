# Parâmetro de Pontuação

O scikit-learn fornece um parâmetro `scoring` em várias ferramentas de avaliação de modelos, como validação cruzada e busca em grade. O parâmetro `scoring` controla a métrica aplicada aos estimadores durante a avaliação.

Aqui está um exemplo de como usar o parâmetro `scoring` com validação cruzada:

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()

scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print("Scores:", scores)
```
