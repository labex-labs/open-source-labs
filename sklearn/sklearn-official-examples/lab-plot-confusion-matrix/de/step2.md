# Daten laden

Wir werden den Iris-Datensatz aus scikit-learn verwenden. Der Datensatz enthält 150 Proben, jede mit vier Merkmalen und einem Ziel-Label.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
```
