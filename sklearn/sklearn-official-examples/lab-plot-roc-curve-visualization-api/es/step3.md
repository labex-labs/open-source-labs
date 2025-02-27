# Entrenar un Bosque Aleatorio y Trazar la Curva ROC

En este paso, entrenaremos un clasificador de bosque aleatorio y graficaremos su curva ROC junto con la curva ROC del SVC. Para hacer esto, crearemos un nuevo objeto `RandomForestClassifier`, lo ajustaremos a los datos de entrenamiento y luego crearemos un nuevo objeto `RocCurveDisplay` utilizando este clasificador. También pasaremos el parámetro `ax` a esta función para graficar las curvas en el mismo eje. Finalmente, llamaremos al método `plot()` del objeto `svc_disp` para graficar la curva ROC del SVC.

```python
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=10, random_state=42)
rfc.fit(X_train, y_train)

ax = plt.gca()
rfc_disp = RocCurveDisplay.from_estimator(rfc, X_test, y_test, ax=ax, alpha=0.8)
svc_disp.plot(ax=ax, alpha=0.8)
plt.show()
```
