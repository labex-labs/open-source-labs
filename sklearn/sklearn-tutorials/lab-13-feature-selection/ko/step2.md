# 단변량 특징 선택

단변량 특징 선택은 단변량 통계 검정을 기반으로 최상의 특징을 선택하는 방식입니다. scikit-learn 에는 단변량 특징 선택을 구현하는 여러 클래스가 있습니다.

- `SelectKBest`: 상위 k 개의 점수가 높은 특징을 선택합니다.
- `SelectPercentile`: 사용자가 지정한 상위 백분위 점수의 특징을 선택합니다.
- `SelectFpr`: 거짓 양성률을 기반으로 특징을 선택합니다.
- `SelectFdr`: 거짓 발견률을 기반으로 특징을 선택합니다.
- `SelectFwe`: 가족별 오류율을 기반으로 특징을 선택합니다.
- `GenericUnivariateSelect`: 구성 가능한 전략으로 선택을 허용합니다.

다음은 Iris 데이터 세트에서 상위 2 개의 특징을 선택하기 위한 `SelectKBest` 사용 예입니다.

```python
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# Iris 데이터 세트를 로드합니다.
X, y = load_iris(return_X_y=True)

# f_classif 점수 함수와 k=2 로 SelectKBest 를 초기화합니다.
selector = SelectKBest(f_classif, k=2)

# 최상의 특징을 선택합니다.
X_selected = selector.fit_transform(X, y)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", selector.get_support(indices=True))
```

이 예제에서는 `f_classif` 점수 함수를 사용하여 Iris 데이터 세트에서 상위 2 개의 특징을 선택합니다. 출력은 데이터 세트의 원래 모양과 최상의 특징을 선택한 후의 모양을 보여줄 것입니다.
