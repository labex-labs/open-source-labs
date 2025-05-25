# 막대 그래프 데이터 생성

이제 막대 그래프에 대한 데이터를 생성합니다. 각 20 개의 값을 가진 네 개의 데이터 세트를 생성합니다. NumPy 의 `arange()` 메서드를 사용하여 20 개의 값 배열을 생성하고, NumPy 의 `random.rand()` 메서드를 사용하여 각 데이터 세트에 대한 임의의 값을 생성합니다.

```python
colors = ['r', 'g', 'b', 'y']
yticks = [3, 2, 1, 0]
for c, k in zip(colors, yticks):
    xs = np.arange(20)
    ys = np.random.rand(20)
```
