# 데이터 생성

이 실습에서는 소규모 데이터셋을 생성합니다. 훈련 샘플 500 개, 테스트 샘플 20 개, 이상치 샘플 20 개를 생성합니다.

```python
random_state = 42
rng = np.random.RandomState(random_state)

# 훈련 데이터 생성
X = 0.3 * rng.randn(500, 2)
X_train = np.r_[X + 2, X - 2]
# 일반적인 새로운 관측치 생성
X = 0.3 * rng.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
# 이상치 새로운 관측치 생성
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))
```
