# 다양한 유형의 플롯 생성

Matplotlib 은 선 그래프, 산점도, 막대 그래프 등 다양한 플롯 유형을 지원합니다. 다음은 산점도를 생성하는 예제 코드입니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# Create a scatter plot
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

# Display the plot
plt.show()
```

이 코드에서는 `scatter()` 메서드를 사용하여 산점도를 생성합니다. NumPy 라이브러리를 사용하여 일부 임의의 데이터를 생성하고 이를 `scatter()` 메서드에 전달합니다. 또한 `c` 매개변수를 사용하여 데이터 포인트의 색상을 지정하고, `s` 매개변수를 사용하여 데이터 포인트의 크기를 지정하며, `alpha` 매개변수를 사용하여 데이터 포인트의 투명도를 지정합니다.
