# Modell erstellen und trainieren mit Early Stopping

Wir werden nun ein Gradient Boosting-Modell mit Early Stopping erstellen und trainieren. Wir geben einen `validation_fraction` an, der den Anteil des gesamten Datensatzes angibt, der von der Trainingsphase abgesondert wird, um die Validierungsverlustfunktion des Modells zu bewerten. Das Gradient Boosting-Modell wird mit dem Trainingssatz trainiert und mit dem Validierungssatz ausgewertet. Wenn jeder zusätzliche Stufe des Regressionsbaums hinzugefügt wird, wird der Validierungssatz verwendet, um das Modell zu bewerten. Dies wird fortgesetzt, bis die Bewertungen des Modells in den letzten `n_iter_no_change` Stufen um mindestens `tol` nicht mehr verbessern. Danach wird angenommen, dass das Modell konvergiert ist und die weitere Hinzufügung von Stufen wird "frühzeitig gestoppt". Die Anzahl der Stufen des endgültigen Modells ist über das Attribut `n_estimators` verfügbar.

```python
gbes = ensemble.GradientBoostingClassifier(
        n_estimators=n_estimators,
        validation_fraction=0.2,
        n_iter_no_change=5,
        tol=0.01,
        random_state=0,
    )
start = time.time()
gbes.fit(X_train, y_train)
time_gbes.append(time.time() - start)
```
