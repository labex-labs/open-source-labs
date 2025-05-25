# 테스트 데이터 포인트 생성

-1 과 1 사이의 x 및 y 값을 갖는 일련의 임의 테스트 데이터 포인트를 생성합니다. 또한 2 단계에서 정의된 `experiment_res` 함수를 사용하여 해당 z 값 집합을 생성합니다.

```python
# User parameters for data test points

# Number of test data points, tested from 3 to 5000 for subdiv=3
n_test = 200

# Random points
random_gen = np.random.RandomState(seed=19680801)
x_test = random_gen.uniform(-1., 1., size=n_test)
y_test = random_gen.uniform(-1., 1., size=n_test)
z_test = experiment_res(x_test, y_test)
```
