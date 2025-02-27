# Das Verständnis von Datensätzen

Scikit-learn repräsentiert Datensätze als 2D-Arrays, wobei die erste Achse die Proben und die zweite Achse die Merkmale repräsentiert. Schauen wir uns ein Beispiel mit dem Iris-Datensatz an:

```python
from sklearn import datasets

iris = datasets.load_iris()
data = iris.data
print(data.shape)
```

Ausgabe:

```
(150, 4)
```

Der Iris-Datensatz besteht aus 150 Beobachtungen von Irisen, wobei jede Beobachtung durch 4 Merkmale beschrieben wird. Die Form des Datenarrays ist (150, 4).
