# Daten laden

Als nächstes laden wir den Iris-Datensatz, ein populärer Datensatz in der Maschinellen Lernung. Dieser Datensatz enthält Informationen über die Merkmale verschiedener Arten von Iris-Blumen. Wir werden diesen Datensatz verwenden, um den K-Means-Clustering-Algorithmus zu demonstrieren.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```
