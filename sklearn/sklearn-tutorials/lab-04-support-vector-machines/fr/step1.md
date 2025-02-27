# Classification avec SVM

- Commencez par importer les bibliothèques nécessaires :

```python
from sklearn import svm
```

- Définissez les échantillons d'entraînement `X` et les étiquettes de classe `y` :

```python
X = [[0, 0], [1, 1]]
y = [0, 1]
```

- Créez une instance du classifieur `SVC` et ajustez les données :

```python
clf = svm.SVC()
clf.fit(X, y)
```

- Utilisez le modèle entraîné pour prédire de nouvelles valeurs :

```python
clf.predict([[2., 2.]])
```
