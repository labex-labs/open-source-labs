# Создание экземпляра логистической регрессии и подгонка данных

Мы создадим экземпляр логистической регрессии и подгоним данные.

```python
# Create an instance of Logistic Regression Classifier and fit the data.
logreg = LogisticRegression(C=1e5)
logreg.fit(X, Y)
```
