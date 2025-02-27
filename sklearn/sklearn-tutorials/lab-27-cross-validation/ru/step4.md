# Обучаем и оцениваем модель

Теперь обучим классификатор на основе методов опорных векторов (SVM) на обучающем наборе и оценим его производительность на тестовом наборе.

```python
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
score = clf.score(X_test, y_test)
print("Accuracy: ", score)
```
