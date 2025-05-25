# 학습 및 테스트 데이터셋 생성

데이터셋을 1000 개의 샘플을 가진 학습 데이터셋과 100 개의 샘플을 가진 테스트 데이터셋으로 분할합니다. 테스트 데이터셋에 가우시안 잡음을 추가하고 원본 데이터의 두 개 복사본을 생성합니다. 하나는 잡음이 있고 하나는 잡음이 없는 데이터입니다.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=0, train_size=1_000, test_size=100
)

rng = np.random.RandomState(0)
noise = rng.normal(scale=0.25, size=X_test.shape)
X_test_noisy = X_test + noise

noise = rng.normal(scale=0.25, size=X_train.shape)
X_train_noisy = X_train + noise
```
