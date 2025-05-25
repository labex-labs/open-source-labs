# 자기지도 분류기 설정

레이블 데이터의 비율이 다른 두 개의 자기지도 분류기를 설정합니다: 30% 와 50%. 자기지도는 레이블이 지정된 데이터로 분류기를 학습시킨 다음, 이를 사용하여 레이블이 지정되지 않은 데이터의 레이블을 예측하는 반지도 학습 알고리즘입니다. 가장 확신 있는 예측 결과는 레이블이 지정된 데이터에 추가되고, 수렴될 때까지 이 과정이 반복됩니다.

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC

# 자기지도 분류기 설정
base_classifier = SVC(kernel="rbf", gamma=0.5, probability=True)
st30 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_30),
    y_30,
    "자기지도 30% 데이터",
)
st50 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_50),
    y_50,
    "자기지도 50% 데이터",
)
```
