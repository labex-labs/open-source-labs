# Trainieren und Evaluieren des Modells

Lassen Sie uns nun einen Support-Vector-Machine (SVM)-Classifier auf dem Trainingsset trainieren und seine Leistung auf dem Testset evaluieren.

```python
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
score = clf.score(X_test, y_test)
print("Accuracy: ", score)
```
