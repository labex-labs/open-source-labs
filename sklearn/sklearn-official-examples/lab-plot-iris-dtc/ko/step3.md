# 의사결정 트리 구조 표시

다음으로, 아이리스 데이터셋의 모든 특징으로 학습된 단일 의사결정 트리의 구조를 표시합니다.

```python
from sklearn.tree import plot_tree

plt.figure()
clf = DecisionTreeClassifier().fit(iris.data, iris.target)
plot_tree(clf, filled=True)
plt.title("모든 아이리스 특징으로 학습된 의사결정 트리")
plt.show()
```
