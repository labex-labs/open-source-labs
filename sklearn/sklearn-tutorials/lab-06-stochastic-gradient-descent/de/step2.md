# Daten laden

Als nächstes werden wir den Iris-Datensatz aus scikit-learn laden. Dieser Datensatz ist ein klassischer Datensatz für maschinelles Lernen, der aus Messungen von Schwertlilienblumen sowie deren Artenbezeichnungen besteht.

```python
iris = load_iris()
X = iris.data
y = iris.target
```
