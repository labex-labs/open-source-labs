# Verbesserung des Modells

Wenn die Genauigkeit unseres Modells nicht zufriedenstellend ist, können wir versuchen, es zu verbessern, indem wir die Hyperparameter des SVM-Algorithmus optimieren. Beispielsweise können wir versuchen, den Wert des Parameters `C` zu ändern:

```python
# Erstellen Sie den SVM-Klassifizierer mit einem anderen Wert von C
clf = SVC(kernel='linear', C=0.1)

# Trainieren Sie den Klassifizierer auf den Trainingsdaten
clf.fit(X_train, y_train)

# Vorhersagen der Labels des Testsets
y_pred = clf.predict(X_test)

# Berechnung der Genauigkeit des Modells
accuracy = accuracy_score(y_test, y_pred)

# Ausgabe der Genauigkeit des Modells
print("Genauigkeit:", accuracy)
```
