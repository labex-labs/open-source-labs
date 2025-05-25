# 역변환

랜덤 투영 변환기는 투영 행렬의 역행렬을 계산할 수 있는 옵션을 제공합니다. 투영된 데이터에 역변환을 적용하여 이 기능을 살펴보겠습니다.

```python
transformer = random_projection.SparseRandomProjection(compute_inverse_components=True)
X_new = transformer.fit_transform(X)

# 역변환 계산
X_new_inversed = transformer.inverse_transform(X_new)
```

이 단계에서 `compute_inverse_components` 매개변수를 `True`로 설정한 `SparseRandomProjection` 클래스의 인스턴스를 생성합니다. 그런 다음 변환기를 데이터 `X`에 맞추고 변환을 적용합니다. 마지막으로, 투영된 데이터 `X_new`에 `inverse_transform` 메서드를 호출하여 역변환을 계산합니다.
