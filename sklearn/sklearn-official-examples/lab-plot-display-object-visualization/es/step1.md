# Cargar datos y entrenar el modelo

Para este ejemplo, usaremos un conjunto de datos de un centro de servicios de donación de sangre de OpenML. La variable objetivo es si una persona donó sangre. Primero, los datos se dividen en conjuntos de entrenamiento y prueba, y luego se ajusta un modelo de regresión logística con el conjunto de entrenamiento.

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=1464, return_X_y=True, parser="pandas")
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)

clf = make_pipeline(StandardScaler(), LogisticRegression(random_state=0))
clf.fit(X_train, y_train)
```
