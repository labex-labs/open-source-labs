# 데이터 준비

근사하려는 함수를 정의하고 플롯을 준비하는 것으로 시작합니다.

```python
def f(x):
    """다항 보간으로 근사할 함수."""
    return x * np.sin(x)

# 플롯하고자 하는 전체 범위
x_plot = np.linspace(-1, 11, 100)

# 흥미를 위해 학습에 사용할 점의 작은 부분집합만 제공합니다.
x_train = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
x_train = np.sort(rng.choice(x_train, size=20, replace=False))
y_train = f(x_train)

# 변환기에 입력하기 위해 이러한 배열의 2 차원 배열 버전을 만듭니다.
X_train = x_train[:, np.newaxis]
X_plot = x_plot[:, np.newaxis]
```
