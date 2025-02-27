# Tracer la courbe ROC

Ensuite, nous allons tracer la courbe ROC à l'aide de la fonction `RocCurveDisplay.from_estimator`. Cette fonction prend le classifieur entraîné, l'ensemble de données de test et les vraies étiquettes en entrée, et renvoie un objet qui peut être utilisé pour tracer la courbe ROC. Nous appellerons ensuite la méthode `show()` pour afficher le tracé.

```python
svc_disp = RocCurveDisplay.from_estimator(svc, X_test, y_test)
svc_disp.show()
```
