# 낮은 분산을 가진 특징 제거

scikit-learn 의 `VarianceThreshold` 클래스는 낮은 분산을 가진 특징을 제거하는 데 사용될 수 있습니다. 낮은 분산을 가진 특징은 일반적으로 모델에 많은 정보를 제공하지 않습니다. `VarianceThreshold`를 사용하여 0 분산 특징을 제거하는 방법을 보여 드리겠습니다.

```python
from sklearn.feature_selection import VarianceThreshold

X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]

# 80% 의 변동성을 갖는 임계값으로 VarianceThreshold 를 초기화합니다.
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))

# 높은 변동성을 가진 특징을 선택합니다.
X_selected = sel.fit_transform(X)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", sel.get_support(indices=True))
```

이 코드 조각은 `VarianceThreshold`를 사용하여 데이터 세트에서 0 분산 특징을 제거하는 방법을 보여줍니다. 출력은 데이터 세트의 원래 모양과 높은 변동성을 가진 특징을 선택한 후의 모양을 보여줄 것입니다.
