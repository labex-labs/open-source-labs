# Entraîner un forêt aléatoire et tracer la courbe ROC

Dans cette étape, nous allons entraîner un classifieur à forêt aléatoire et tracer sa courbe ROC en même temps que la courbe ROC du SVC. Pour ce faire, nous allons créer un nouvel objet `RandomForestClassifier`, l'ajuster aux données d'entraînement, puis créer un nouvel objet `RocCurveDisplay` en utilisant ce classifieur. Nous passerons également le paramètre `ax` à cette fonction pour tracer les courbes sur le même axe. Enfin, nous appellerons la méthode `plot()` de l'objet `svc_disp` pour tracer la courbe ROC du SVC.

```python
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=10, random_state=42)
rfc.fit(X_train, y_train)

ax = plt.gca()
rfc_disp = RocCurveDisplay.from_estimator(rfc, X_test, y_test, ax=ax, alpha=0.8)
svc_disp.plot(ax=ax, alpha=0.8)
plt.show()
```
