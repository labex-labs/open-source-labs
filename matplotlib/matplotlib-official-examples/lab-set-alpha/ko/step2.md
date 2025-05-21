# 균일한 알파 값으로 막대 차트 만들기

이 단계에서는 `alpha` 키워드 인수를 사용하여 모든 막대가 동일한 투명도 수준을 갖는 막대 차트를 만듭니다.

## 새 셀 추가

도구 모음에서 "+" 버튼을 클릭하거나 명령 모드에서 "Esc"를 누른 다음 "b"를 눌러 Jupyter Notebook 에 새 셀을 추가합니다.

## 균일한 알파로 막대 차트 만들기

새 셀에 다음 코드를 입력하고 실행합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Create the bar chart with alpha=0.5 for all bars
ax.bar(x_values, y_values, color=facecolors, edgecolor=edgecolors, alpha=0.5)

# Add a title and labels
ax.set_title("Bar Chart with Uniform Alpha Value (alpha=0.5)")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## 코드 및 출력 이해하기

코드를 실행한 후 20 개의 막대가 있는 막대 차트가 표시되어야 합니다. 각 막대는 동일한 투명도 수준 (alpha=0.5) 으로 녹색 (양수 y 값) 또는 빨간색 (음수 y 값) 입니다.

주요 부분을 분석해 보겠습니다.

1. `np.random.seed(19680801)` - 이 코드는 코드를 실행할 때마다 생성되는 난수가 동일하도록 보장합니다.

2. `x_values = list(range(20))` - x 축에 대해 0 에서 19 까지의 정수 목록을 만듭니다.

3. `y_values = np.random.randn(20)` - y 축에 대해 표준 정규 분포에서 20 개의 임의 값을 생성합니다.

4. `facecolors = ['green' if y > 0 else 'red' for y in y_values]` - 이 리스트 컴프리헨션은 양수 값에 녹색을, 음수 값에 빨간색을 할당합니다.

5. `ax.bar(..., alpha=0.5)` - 모든 막대에 대해 균일한 알파 값 0.5 를 설정하는 핵심 부분입니다.

균일한 알파 값은 모든 막대를 동일하게 투명하게 만들며, 다음과 같은 경우에 유용할 수 있습니다.

- 막대를 통해 배경 격자선을 표시하려는 경우
- 더 미묘한 시각화를 만들려는 경우
- 모든 요소의 시각적 지배력을 동일하게 줄이려는 경우

다음 단계에서는 서로 다른 막대에 대해 서로 다른 알파 값을 설정하는 방법을 살펴보겠습니다.
