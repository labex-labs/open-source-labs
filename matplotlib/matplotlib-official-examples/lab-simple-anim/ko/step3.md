# 데이터 생성

이 단계에서는 선 그래프에 대한 데이터를 생성합니다. NumPy 의 `arange()` 함수를 사용하여 x 축 값의 배열을 생성하고, `sin()` 함수를 사용하여 사인파의 y 축 값 배열을 생성합니다.

```python
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))
```
