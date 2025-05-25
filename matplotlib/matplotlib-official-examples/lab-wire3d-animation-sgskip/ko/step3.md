# Meshgrid 생성

세 번째 단계는 `linspace`를 사용하여 meshgrid 를 생성하는 것입니다.

```python
xs = np.linspace(-1, 1, 50)
ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)
```
