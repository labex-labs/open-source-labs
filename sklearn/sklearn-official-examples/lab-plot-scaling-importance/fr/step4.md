# Effet de la mise à l'échelle sur les performances du modèle

Nous allons entraîner un modèle de régression logistique avec des données réduites par PCA pour évaluer l'effet de la mise à l'échelle des fonctionnalités sur les performances du modèle. Nous comparerons les performances du modèle avec des fonctionnalités non mises à l'échelle et mises à l'échelle.

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

print("Précision sur le test pour la PCA non mise à l'échelle")
print(f"{accuracy_score(y_test, y_pred):.2%}\n")
print("Précision sur le test pour les données standardisées avec PCA")
print(f"{accuracy_score(y_test, y_pred_scaled):.2%}\n")
print("Perte logarithmique pour la PCA non mise à l'échelle")
print(f"{log_loss(y_test, y_proba):.3}\n")
print("Perte logarithmique pour les données standardisées avec PCA")
print(f"{log_loss(y_test, y_proba_scaled):.3}")
```
