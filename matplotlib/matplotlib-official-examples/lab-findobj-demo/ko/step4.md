# 플롯 사용자 정의

Matplotlib 은 플롯에 대한 광범위한 사용자 정의 옵션을 제공합니다. 다음은 간단한 선 그래프를 사용자 정의하는 예제 코드입니다.

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y, color='red', linewidth=2, linestyle='--', marker='o', markersize=8, markerfacecolor='yellow')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Plot')

# Display the plot
plt.show()
```

이 코드에서는 `plot()` 메서드의 다양한 매개변수를 사용하여 플롯을 사용자 정의합니다. 선의 색상을 빨간색으로, 선 너비를 2 로, 선 스타일을 점선 (`--`) 으로, 마커를 원 (`o`) 으로, 마커 크기를 8 로, 마커 채우기 색상을 노란색으로 변경합니다.
