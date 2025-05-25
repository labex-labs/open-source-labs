# Exibir a Estrutura da Árvore de Decisão

Em seguida, exibiremos a estrutura de uma única árvore de decisão treinada em todas as características do conjunto de dados Iris.

```python
from sklearn.tree import plot_tree

plt.figure()
clf = DecisionTreeClassifier().fit(iris.data, iris.target)
plot_tree(clf, filled=True)
plt.title("Árvore de decisão treinada em todas as características do conjunto de dados Iris")
plt.show()
```
