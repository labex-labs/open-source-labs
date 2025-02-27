# Clasificación con SVM

- Comience importando las bibliotecas necesarias:

```python
from sklearn import svm
```

- Defina las muestras de entrenamiento `X` y las etiquetas de clase `y`:

```python
X = [[0, 0], [1, 1]]
y = [0, 1]
```

- Cree una instancia del clasificador `SVC` y ajuste los datos:

```python
clf = svm.SVC()
clf.fit(X, y)
```

- Utilice el modelo entrenado para predecir nuevos valores:

```python
clf.predict([[2., 2.]])
```
