# Treinar e testar o classificador de Regressão Logística

Agora, treinaremos um classificador de Regressão Logística usando a função `LogisticRegression` do scikit-learn e testaremos-o no conjunto de teste. Em seguida, imprimiremos a pontuação de precisão do classificador.

```python
from sklearn.linear_model import LogisticRegression

logistic = LogisticRegression(max_iter=1000)
logistic.fit(X_train, y_train)
logistic_score = logistic.score(X_test, y_test)

print("Logistic Regression score: %f" % logistic_score)
```
