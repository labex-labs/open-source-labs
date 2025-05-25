# 재귀적 특징 제거 (RFE)

재귀적 특징 제거 (RFE) 는 특징의 중요도를 순차적으로 평가하여 가장 중요한 특징을 선택하는 특징 선택 방법입니다. 특징에 가중치를 할당하여 외부 추정기를 학습시키고, 가장 중요하지 않은 특징을 제거하는 방식으로 작동합니다.

```python
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE

# Iris 데이터셋을 로드합니다.
X, y = load_iris(return_X_y=True)

# SVC 를 외부 추정기로 초기화합니다.
estimator = SVC(kernel="linear")

# 외부 추정기와 2 개의 특징을 선택할 수 있도록 RFE 를 초기화합니다.
selector = RFE(estimator, n_features_to_select=2)

# 최상의 특징을 선택합니다.
X_selected = selector.fit_transform(X, y)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", selector.get_support(indices=True))
```

이 예제에서는 지원 벡터 분류기 (SVC) 를 외부 추정기로 사용하여 Iris 데이터 세트에서 상위 2 개의 특징을 선택합니다. 출력은 데이터 세트의 원래 모양과 최상의 특징을 선택한 후의 모양을 보여줄 것입니다.
