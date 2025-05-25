# 적절한 Alpha 값 결정

의사 결정 트리 가지치기에 사용할 적절한 alpha 값을 결정하고자 합니다. 이는 가지치기된 트리의 효과적인 alpha 값 대비 잎 노드의 총 불순도를 플롯하여 수행할 수 있습니다.

```python
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

clf = DecisionTreeClassifier(random_state=0)
path = clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

fig, ax = plt.subplots()
ax.plot(ccp_alphas[:-1], impurities[:-1], marker="o", drawstyle="steps-post")
ax.set_xlabel("효과적인 alpha")
ax.set_ylabel("잎 노드의 총 불순도")
ax.set_title("학습 데이터셋의 총 불순도 대 효과적인 alpha")
```
