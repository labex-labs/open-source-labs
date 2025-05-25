# 데이터 생성

`np.meshgrid()` 함수를 사용하여 `X` 및 `Y` 좌표를 생성해야 합니다. 그런 다음, 벡터 필드를 나타내는 `U` 및 `V` 배열을 생성합니다.

```python
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)
```
