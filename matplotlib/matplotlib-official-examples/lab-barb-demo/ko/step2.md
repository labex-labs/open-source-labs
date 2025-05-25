# 데이터 생성

다음으로, 풍향 막대 그래프를 생성하는 데 사용될 데이터를 생성합니다. 5x5 의 균일한 그리드와 meshgrid 및 곱셈 함수를 사용하여 벡터 필드를 생성합니다.

```python
x = np.linspace(-5, 5, 5)
X, Y = np.meshgrid(x, x)
U, V = 12 * X, 12 * Y
```
