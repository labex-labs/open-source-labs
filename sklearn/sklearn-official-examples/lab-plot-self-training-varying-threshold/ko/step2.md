# 데이터 로드

```python
X, y = datasets.load_breast_cancer(return_X_y=True)
X, y = shuffle(X, y, random_state=42)
y_true = y.copy()
y[50:] = -1
total_samples = y.shape[0]
```

`breast_cancer` 데이터셋을 로드하고 섞습니다. 그런 다음 실제 레이블을 `y_true`에 복사하고 `y`에서 처음 50 개 샘플을 제외한 모든 레이블을 제거합니다. 이는 준지도 학습 시나리오를 시뮬레이션하는 데 사용됩니다.
