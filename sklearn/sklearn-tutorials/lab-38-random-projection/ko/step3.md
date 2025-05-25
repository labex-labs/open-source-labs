# 가우시안 랜덤 투영

이제 가우시안 랜덤 투영을 적용하여 데이터의 차원을 줄여 보겠습니다.

```python
transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
```

이 단계에서 `GaussianRandomProjection` 클래스의 인스턴스를 생성하고 데이터 `X`에 맞춥니다. 그런 다음 `fit_transform` 메서드를 호출하여 변환을 적용합니다. 결과는 `X_new` 변수에 저장됩니다.
