# 간단한 플롯 생성

Matplotlib 에서 가장 기본적인 플롯은 선 그래프입니다. `plot()` 메서드를 사용하여 선 그래프를 생성할 수 있습니다. 다음은 간단한 선 그래프를 생성하는 예제 코드입니다.

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')

# Display the plot
plt.show()
```

이 코드에서는 먼저 데이터 포인트를 `x`와 `y`라는 두 개의 리스트로 정의합니다. 그런 다음 `plot()` 메서드를 사용하여 플롯을 생성하고 데이터 포인트를 전달합니다. 그 후 `xlabel()`, `ylabel()`, 및 `title()` 메서드를 사용하여 X 및 Y 축에 레이블을 추가하고 플롯에 제목을 추가합니다. 마지막으로 `show()` 메서드를 사용하여 플롯을 표시합니다.
