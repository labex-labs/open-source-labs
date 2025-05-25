# 희소 랜덤 투영

다음으로, 희소 랜덤 투영이라는 다른 유형의 랜덤 투영을 시도해 보겠습니다.

```python
transformer = random_projection.SparseRandomProjection()
X_new = transformer.fit_transform(X)
```

여기서 `SparseRandomProjection` 클래스의 인스턴스를 생성하고 `fit_transform` 메서드를 사용하여 데이터 `X`에 적용합니다. 결과는 `X_new` 변수에 저장됩니다.
