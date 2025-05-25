# 데이터 생성

다음으로 두 개의 구성 요소를 가진 가우시안 혼합 데이터셋을 생성합니다. (20, 20) 에 중심이 놓인 이동된 가우시안 데이터셋과 원점 중심의 늘어난 가우시안 데이터셋을 생성합니다. 그런 다음 두 데이터셋을 연결하여 최종 학습 데이터셋을 만듭니다.

```python
n_samples = 300

# 랜덤 샘플 생성, 두 개의 구성 요소
np.random.seed(0)

# (20, 20) 에 중심이 놓인 구형 데이터 생성
shifted_gaussian = np.random.randn(n_samples, 2) + np.array([20, 20])

# 원점 중심의 늘어난 가우시안 데이터 생성
C = np.array([[0.0, -0.7], [3.5, 0.7]])
stretched_gaussian = np.dot(np.random.randn(n_samples, 2), C)

# 두 데이터셋을 연결하여 최종 학습 데이터셋 생성
X_train = np.vstack([shifted_gaussian, stretched_gaussian])
```
