# Afficher la structure de l'arbre de décision

Ensuite, nous allons afficher la structure d'un seul arbre de décision entraîné sur toutes les caractéristiques de l'ensemble de données Iris.

```python
from sklearn.tree import plot_tree

plt.figure()
clf = DecisionTreeClassifier().fit(iris.data, iris.target)
plot_tree(clf, filled=True)
plt.title("Arbre de décision entraîné sur toutes les caractéristiques de l'iris")
plt.show()
```
