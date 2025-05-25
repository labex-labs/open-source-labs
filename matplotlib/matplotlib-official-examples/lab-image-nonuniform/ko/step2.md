# 선형 및 비선형 배열 생성

두 개의 배열을 생성해야 합니다. 하나는 선형 값, 다른 하나는 비선형 값을 갖습니다. 이 배열은 NonUniformImage 를 생성하는 데 사용됩니다.

```python
# 셀 중심에 대한 선형 x 배열:
x = np.linspace(-4, 4, 9)

# 고도로 비선형 x 배열:
x2 = x**3

y = np.linspace(-4, 4, 9)

z = np.sqrt(x[np.newaxis, :]**2 + y[:, np.newaxis]**2)
```
