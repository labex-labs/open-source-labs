# SelectFromModel 을 이용한 특징 선택

`SelectFromModel` 클래스는 각 특징에 중요도를 할당하는 모든 추정기와 함께 사용할 수 있는 메타 변환기입니다. 특징의 중요도를 기반으로 특징을 선택하고, 지정된 임계값보다 낮은 특징을 제거합니다.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel

# Iris 데이터셋을 로드합니다.
X, y = load_iris(return_X_y=True)

# 추정기로 RandomForestClassifier 를 초기화합니다.
estimator = RandomForestClassifier()

# 추정기와 "평균" 임계값을 사용하여 SelectFromModel 을 초기화합니다.
selector = SelectFromModel(estimator, threshold="mean")

# 최상의 특징을 선택합니다.
X_selected = selector.fit_transform(X, y)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", selector.get_support(indices=True))
```

이 예제에서는 Random Forest 분류기를 추정기로 사용하고, 평균 중요도보다 높은 중요도를 가진 특징을 선택합니다. 출력은 데이터 세트의 원래 모양과 최상의 특징을 선택한 후의 모양을 보여줄 것입니다.
