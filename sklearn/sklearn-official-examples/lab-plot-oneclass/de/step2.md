# Anpassen des One-Class SVM-Modells

Als nächstes werden wir das One-Class SVM-Modell an den generierten Daten anpassen.

```python
# Anpassen des Modells
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)

# Vorhersagen der Labels für die Trainingsdaten, die regulären neuartigen Beobachtungen und die abnormen neuartigen Beobachtungen
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
```
