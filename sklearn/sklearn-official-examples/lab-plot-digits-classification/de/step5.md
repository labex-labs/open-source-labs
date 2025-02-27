# Den Support-Vector-Maschinen trainieren

Wir werden einen Support-Vector-Klassifizierer auf den Trainingsbeispielen mit der `svm.SVC()`-Methode aus `sklearn` trainieren.

```python
clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)
```
