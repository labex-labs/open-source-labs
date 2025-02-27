# Modell trainieren

Wir werden einen Support-Vector-Machine (SVM)-Classifier mit einem linearen Kernel trainieren. Wir werden einen Regularisierungsparameter C verwenden, der zu niedrig ist, um die Auswirkungen auf die Ergebnisse zu sehen.

```python
classifier = svm.SVC(kernel="linear", C=0.01).fit(X_train, y_train)
```
