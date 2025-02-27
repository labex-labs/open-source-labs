# Laden des Datensatzes

Als nächstes werden wir den Iris-Datensatz laden. Dieser Datensatz enthält Informationen über vier Merkmale von drei verschiedenen Arten von Irisblumen. Wir werden diesen Datensatz verwenden, um unseren Entscheidungsbaum-Klassifikator (Decision Tree classifier) zu trainieren.

```python
# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
```
