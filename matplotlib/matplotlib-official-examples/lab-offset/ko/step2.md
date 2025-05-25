# 데이터 생성

다음으로, 플롯에 사용할 데이터를 생성합니다. 이 예제에서는 NumPy 를 사용하여 데이터를 생성합니다.

```python
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
```
