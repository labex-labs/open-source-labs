# 순차적 특징 선택을 이용한 특징 선택

순차적 특징 선택기 (SFS) 를 사용하여 특징을 선택합니다. SFS 는 각 반복에서 교차 검증 점수를 기반으로 선택된 특징에 추가할 최상의 새로운 특징을 선택하는 탐욕적 절차입니다. 또한 역방향 (역방향 SFS) 으로 진행할 수 있습니다. 즉, 모든 특징으로 시작하여 하나씩 제거할 특징을 탐욕적으로 선택합니다.

```python
from sklearn.feature_selection import SequentialFeatureSelector

sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="forward").fit(X, y)
sfs_backward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="backward").fit(X, y)

print(f"순방향 순차적 선택으로 선택된 특징: {feature_names[sfs_forward.get_support()]}")
print(f"역방향 순차적 선택으로 선택된 특징: {feature_names[sfs_backward.get_support()]}")
```
