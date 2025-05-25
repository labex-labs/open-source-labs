# 중요도 기반 특징 선택

`SelectFromModel`을 사용하여 계수에 따른 가장 중요한 두 개의 특징을 선택합니다. `SelectFromModel`은 `threshold` 매개변수를 받으며, 이 매개변수보다 중요도 (계수로 정의됨) 가 높은 특징을 선택합니다.

```python
from sklearn.feature_selection import SelectFromModel

threshold = np.sort(importance)[-3] + 0.01

sfm = SelectFromModel(ridge, threshold=threshold).fit(X, y)
print(f"SelectFromModel 이 선택한 특징: {feature_names[sfm.get_support()]}")
```
