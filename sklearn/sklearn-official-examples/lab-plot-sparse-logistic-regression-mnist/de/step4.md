# Modell trainieren

Wir werden das Modell mit Logistischer Regression mit L1-Strafe und SAGA-Algorithmus trainieren. Wir werden den Wert von `C` auf 50,0 geteilt durch die Anzahl der Trainingsbeispiele setzen.

```python
# Turn up tolerance for faster convergence
clf = LogisticRegression(C=50.0 / train_samples, penalty="l1", solver="saga", tol=0.1)
clf.fit(X_train, y_train)
```
