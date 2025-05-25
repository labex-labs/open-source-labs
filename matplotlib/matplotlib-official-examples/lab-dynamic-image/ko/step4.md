# 데이터 생성

Numpy 라이브러리의 `linspace` 메서드를 사용하여 애니메이션에 대한 데이터를 생성할 것입니다. x 와 y, 두 개의 데이터 세트를 생성한 다음, y 데이터를 재구성하여 2 차원 배열을 만들 것입니다.

```python
x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
```
