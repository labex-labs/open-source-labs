# Обучение и тестирование классификатора Логистическая регрессия

Теперь мы обучим классификатор Логистическая регрессия с использованием функции `LogisticRegression` из scikit-learn и протестируем его на тестовой выборке. Затем мы выведем показатель точности классификатора.

```python
from sklearn.linear_model import LogisticRegression

logistic = LogisticRegression(max_iter=1000)
logistic.fit(X_train, y_train)
logistic_score = logistic.score(X_test, y_test)

print("Logistic Regression score: %f" % logistic_score)
```
