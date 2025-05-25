# 데이터 생성

이 단계에서는 평균과 공분산이 다른 두 개의 가우시안 분포로 구성된 샘플 데이터셋을 생성합니다.

```python
n_samples = 500

np.random.seed(0)
C = np.array([[0.0, -0.1], [1.7, 0.4]])
X = np.r_[
    np.dot(np.random.randn(n_samples, 2), C),
    0.7 * np.random.randn(n_samples, 2) + np.array([-6, 3]),
]
```
