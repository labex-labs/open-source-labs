# 단변량 특징 선택

다음으로, F-검정을 사용하여 단변량 특징 선택을 수행합니다. 기본 선택 함수를 사용하여 가장 중요한 네 가지 특징을 선택합니다.

```python
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(f_classif, k=4)
selector.fit(X_train, y_train)
scores = -np.log10(selector.pvalues_)
scores /= scores.max()
```
