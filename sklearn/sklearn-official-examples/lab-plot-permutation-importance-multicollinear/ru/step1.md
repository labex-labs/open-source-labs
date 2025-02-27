# Обучить классификатор Случайный лес

Сначала мы загружаем набор данных о раке груди Висconsin и разбиваем его на обучающий и тестовый наборы. Затем мы обучаем классификатор Случайный лес на обучающем наборе и оцениваем его точность на тестовом наборе.

```python
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
print("Accuracy on test data: {:.2f}".format(clf.score(X_test, y_test)))
```
