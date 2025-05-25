# 데이터셋 생성

이 단계에서는 연속적인 입력 특징과 연속적인 출력 특징을 가진 데이터셋을 생성합니다. `numpy.random.RandomState()` 메서드를 사용하여 입력 특징에 대한 난수를 생성하고 `numpy.sin()` 메서드를 사용하여 출력 특징을 생성합니다.

```python
rnd = np.random.RandomState(42)
X = rnd.uniform(-3, 3, size=100)
y = np.sin(X) + rnd.normal(size=len(X)) / 3
X = X.reshape(-1, 1)
```
