# 데이터 생성

이 단계에서는 `multivariate_normal()` 함수를 사용하여 데이터를 생성해야 합니다. 이 함수는 다변량 정규 분포 (multivariate normal distribution) 에서 랜덤 샘플을 생성합니다.

```python
data = np.vstack([
    multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    multivariate_normal([30, 20], [[3, 1], [1, 3]], size=1000)
])
```
