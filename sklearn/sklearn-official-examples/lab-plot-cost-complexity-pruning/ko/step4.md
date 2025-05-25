# 의사 결정 트리 학습

다음으로, 각 효과적인 alpha 값을 사용하여 의사 결정 트리를 학습합니다. `ccp_alphas`의 마지막 값은 전체 트리를 가지치기하여 트리가 단 하나의 노드만 남기는 alpha 값입니다.

```python
clfs = []
for ccp_alpha in ccp_alphas:
    clf = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
    clf.fit(X_train, y_train)
    clfs.append(clf)
print(
    "마지막 트리의 노드 수는: {}이며 ccp_alpha 는 {}입니다.".format(
        clfs[-1].tree_.node_count, ccp_alphas[-1]
    )
)
```
