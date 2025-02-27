# Laden des Datensatzes

Als nächstes laden wir den Iris-Datensatz. Dieser Datensatz enthält Informationen über vier Merkmale von drei verschiedenen Arten von Iris-Blüten. Wir werden diesen Datensatz verwenden, um unseren Entscheidungsbaum-Klassifizierer zu trainieren.

```python
# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
```