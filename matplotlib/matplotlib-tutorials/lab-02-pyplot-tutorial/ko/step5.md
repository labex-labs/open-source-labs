# 선 속성 사용자 정의

Matplotlib 을 사용하면 선 너비, 대시 스타일, 색상과 같은 다양한 선 속성을 사용자 정의할 수 있습니다. 선 속성을 설정하는 몇 가지 방법을 시연해 보겠습니다.

```python
x = np.arange(0, 5, 0.1)
line, = plt.plot(x, np.sin(x), '-')

# Using the Line2D instance's setter method
line.set_linewidth(2.0)  # Set the linewidth property of the line to 2.0

# Using the pyplot.setp function
plt.setp(line, color='r', linewidth=2.0)  # Set the color and linewidth properties using the setp function

plt.show()
```

설명:

- 배열 `x`를 생성하고 `np.sin` 함수를 사용하여 해당 y 값을 계산합니다.
- `plot` 함수는 선 그래프를 생성하기 위해 호출됩니다.
- `Line2D` 인스턴스의 `set` 메서드를 사용하여 선의 선 너비 속성을 2.0 으로 설정합니다.
- 또는, `setp` 함수를 사용하여 키워드 인수를 통해 색상 및 선 너비와 같은 선의 여러 속성을 설정할 수 있습니다.
