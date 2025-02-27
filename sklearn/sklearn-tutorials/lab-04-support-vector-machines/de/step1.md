# Klassifikation mit SVM

- Beginnen Sie mit dem Import der erforderlichen Bibliotheken:

```python
from sklearn import svm
```

- Definieren Sie die Trainingssamples `X` und die Klassenlabels `y`:

```python
X = [[0, 0], [1, 1]]
y = [0, 1]
```

- Erstellen Sie eine Instanz des `SVC`-Klassifizierers und passen Sie die Daten an:

```python
clf = svm.SVC()
clf.fit(X, y)
```

- Verwenden Sie das trainierte Modell, um neue Werte vorherzusagen:

```python
clf.predict([[2., 2.]])
```
