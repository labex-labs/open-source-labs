# Funciones métricas

El módulo `metrics` de scikit-learn implementa varias funciones para evaluar el error de predicción con fines específicos. Estas funciones se pueden utilizar para calcular la calidad de las predicciones hechas por un modelo.

A continuación, se muestra un ejemplo de uso de la función `accuracy_score` del módulo `metrics`:

```python
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LogisticRegression()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```
