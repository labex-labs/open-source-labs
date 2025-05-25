# Funções de Métrica

O módulo `metrics` do scikit-learn implementa várias funções para avaliar o erro de previsão para propósitos específicos. Essas funções podem ser usadas para calcular a qualidade das previsões feitas por um modelo.

Aqui está um exemplo de como usar a função `accuracy_score` do módulo `metrics`:

```python
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LogisticRegression()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Precisão:", accuracy)
```
