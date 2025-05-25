# 랜덤 시드 설정 및 데이터 생성

이 단계에서는 랜덤 시드를 설정하고 데이터를 생성합니다. 평균 200, 표준 편차 25 인 정규 분포에서 100 개의 데이터 포인트를 생성합니다.

```python
np.random.seed(19680801)
mu = 200
sigma = 25
data = np.random.normal(mu, sigma, size=100)
```
