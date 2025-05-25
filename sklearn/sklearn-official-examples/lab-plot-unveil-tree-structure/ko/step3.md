# 의사결정 트리 시각화

scikit-learn 의 `tree` 모듈에서 `plot_tree` 함수를 사용하여 의사결정 트리를 시각화할 수도 있습니다.

```python
from sklearn import tree
import matplotlib.pyplot as plt

tree.plot_tree(clf)
plt.show()
```
