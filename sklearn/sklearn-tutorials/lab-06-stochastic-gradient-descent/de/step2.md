# Daten laden

Als nächstes laden wir den Iris-Datensatz aus scikit-learn. Dieser Datensatz ist ein klassischer Datensatz der Maschinellen Lernung, der Messungen von Iris-Blumen zusammen mit ihren Artbezeichnungen enthält.

```python
iris = load_iris()
X = iris.data
y = iris.target
```