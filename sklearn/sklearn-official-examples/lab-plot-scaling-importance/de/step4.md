# Effekt der Skalierung auf die Modellleistung

Wir werden ein logistisches Regressionsmodell mit PCA-reduzierten Daten trainieren, um den Effekt der Feature-Skalierung auf die Modellleistung zu evaluieren. Wir werden die Leistung des Modells mit nicht skalierten und skalierten Features vergleichen.

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import log_loss

Cs = np.logspace(-5, 5, 20)

unscaled_clf = make_pipeline(pca, LogisticRegressionCV(Cs=Cs))
unscaled_clf.fit(X_train, y_train)

scaled_clf = make_pipeline(scaler, pca, LogisticRegressionCV(Cs=Cs))
scaled_clf.fit(X_train, y_train)

y_pred = unscaled_clf.predict(X_test)
y_pred_scaled = scaled_clf.predict(X_test)
y_proba = unscaled_clf.predict_proba(X_test)
y_proba_scaled = scaled_clf.predict_proba(X_test)

print("Testgenauigkeit für die nicht skalierte PCA")
print(f"{accuracy_score(y_test, y_pred):.2%}\n")
print("Testgenauigkeit für die standardisierten Daten mit PCA")
print(f"{accuracy_score(y_test, y_pred_scaled):.2%}\n")
print("Log-Loss für die nicht skalierte PCA")
print(f"{log_loss(y_test, y_proba):.3}\n")
print("Log-Loss für die standardisierten Daten mit PCA")
print(f"{log_loss(y_test, y_proba_scaled):.3}")
```
