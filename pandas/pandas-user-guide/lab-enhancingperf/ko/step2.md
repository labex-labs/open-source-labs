# 순수 Python 함수 구현

DataFrame 의 행별로 작동하는 순수 Python 함수를 생성하는 것으로 시작합니다.

```python
# Define a function
def f(x):
    return x * (x - 1)

# Define another function that uses the first function
def integrate_f(a, b, N):
       s = 0
       dx = (b - a) / N
       for i in range(N):
           s += f(a + i * dx)
       return s * dx
```
