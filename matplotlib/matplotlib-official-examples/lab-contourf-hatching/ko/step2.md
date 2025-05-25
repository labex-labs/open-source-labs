# 데이터 생성

다음으로, 플롯할 샘플 데이터를 생성합니다. 이 예제에서는 x 및 y 값의 2D 그리드를 생성하고 이를 사용하여 z 값을 계산합니다.

```python
# invent some numbers, turning the x and y arrays into simple
# 2d arrays, which make combining them together easier.
x = np.linspace(-3, 5, 150).reshape(1, -1)
y = np.linspace(-3, 5, 120).reshape(-1, 1)
z = np.cos(x) + np.sin(y)
```
