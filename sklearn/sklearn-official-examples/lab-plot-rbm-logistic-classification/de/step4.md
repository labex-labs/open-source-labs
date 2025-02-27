# Evaluation

In diesem Schritt evaluieren wir die Leistung des Modells auf dem Testdatensatz. Wir verwenden die Funktion `classification_report` aus dem Modul `sklearn.metrics`, um den Klassifikationsbericht sowohl für das Pipeline-Modell als auch für das logistische Regressionsmodell zu generieren.

```python
from sklearn import metrics

Y_pred = rbm_features_classifier.predict(X_test)
print(
    "Logistische Regression mit RBM-Features:\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)

# Direktes Training des logistischen Regressionsklassifizierers auf den Pixeln
raw_pixel_classifier = clone(logistic)
raw_pixel_classifier.C = 100.0
raw_pixel_classifier.fit(X_train, Y_train)

Y_pred = raw_pixel_classifier.predict(X_test)
print(
    "Logistische Regression mit rohen Pixel-Features:\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)
```
