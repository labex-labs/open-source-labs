# Мультиклассовая классификация

- Классификаторы `SVC` и `NuSVC` можно использовать для мультиклассовой классификации с использованием подхода "один против остальных" ("one-versus-one"):

```python
X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, Y)
dec = clf.decision_function([[1]])
```
