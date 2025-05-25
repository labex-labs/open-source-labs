# 샘플 데이터 생성

이 단계에서는 numpy 를 사용하여 샘플 데이터를 생성합니다. 평균 100, 표준 편차 15 인 정규 분포에서 무작위 데이터를 생성합니다.

```python
np.random.seed(19680801)
mu = 100  # 분포의 평균 (mean)
sigma = 15  # 분포의 표준 편차 (standard deviation)
x = mu + sigma * np.random.randn(437)
```
