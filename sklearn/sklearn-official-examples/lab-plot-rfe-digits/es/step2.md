# Crear el objeto RFE y ajustar los datos

A continuación, crearemos un objeto de la clase RFE y ajustaremos los datos a él. Usaremos un clasificador de vectores de soporte (Support Vector Classifier - SVC) con un kernel lineal como estimador. Seleccionaremos una característica a la vez y daremos un paso a la vez.

```python
from sklearn.svm import SVC
from sklearn.feature_selection import RFE

svc = SVC(kernel="linear", C=1)
rfe = RFE(estimator=svc, n_features_to_select=1, step=1)
rfe.fit(X, y)
```
