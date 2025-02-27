# Ein Random Forest Classifier trainieren

Wir laden zunächst den Wisconsin Breast Cancer-Datensatz und teilen ihn in Trainings- und Testsets auf. Anschließend trainieren wir einen Random Forest Classifier auf dem Trainingsset und evaluieren seine Genauigkeit auf dem Testset.

```python
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
print("Accuracy on test data: {:.2f}".format(clf.score(X_test, y_test)))
```
