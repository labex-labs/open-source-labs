# FastICA 알고리즘 사용

이 단계에서는 FastICA 알고리즘을 사용합니다. 이 알고리즘은 특징 공간에서 비정규성이 높은 투영에 해당하는 방향을 찾습니다.

```python
ica = FastICA(random_state=rng, whiten="arbitrary-variance")
S_ica_ = ica.fit(X).transform(X)  # 소스 추정

S_ica_ /= S_ica_.std(axis=0)
```
