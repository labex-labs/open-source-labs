# Zeige die Struktur des Entscheidungsbaums

Als nächstes werden wir die Struktur eines einzelnen Entscheidungsbaums anzeigen, der auf allen Merkmalen des Iris-Datensatzes trainiert wurde.

```python
from sklearn.tree import plot_tree

plt.figure()
clf = DecisionTreeClassifier().fit(iris.data, iris.target)
plot_tree(clf, filled=True)
plt.title("Entscheidungsbaum, der auf allen Iris-Merkmalen trainiert wurde")
plt.show()
```
