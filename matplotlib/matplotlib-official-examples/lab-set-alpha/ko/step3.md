# 가변적인 알파 값으로 막대 차트 만들기

이 단계에서는 `(matplotlib_color, alpha)` 튜플 형식을 사용하여 각 막대의 데이터 값에 따라 서로 다른 투명도 수준을 할당합니다.

## 새 셀 추가

도구 모음에서 "+" 버튼을 클릭하거나 명령 모드에서 "Esc"를 누른 다음 "b"를 눌러 Jupyter Notebook 에 새 셀을 추가합니다.

## 가변적인 알파 값으로 막대 차트 만들기

새 셀에 다음 코드를 입력하고 실행합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data (using the same data as in Step 2 for comparison)
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Calculate alpha values based on the absolute y-values
# Normalize y values to get alpha values between 0.2 and 1.0
abs_y = [abs(y) for y in y_values]
max_abs_y = max(abs_y)
face_alphas = [0.2 + 0.8 * (val / max_abs_y) for val in abs_y]

# Create color-alpha tuples for each bar
colors_with_alphas = list(zip(facecolors, face_alphas))

# Create the bar chart with varying alpha values
ax.bar(x_values, y_values, color=colors_with_alphas, edgecolor=edgecolors)

# Add a title and labels
ax.set_title("Bar Chart with Varying Alpha Values Based on Bar Height")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## 코드 및 출력 이해하기

코드를 실행한 후 20 개의 막대가 있는 막대 차트가 표시되어야 합니다. 각 막대는 절대 y 값에 비례하는 투명도 수준을 갖습니다. 즉, 더 높은 막대는 더 불투명하고, 더 짧은 막대는 더 투명합니다.

코드의 주요 부분을 분석해 보겠습니다.

1. `abs_y = [abs(y) for y in y_values]` - 모든 y 값의 절대값 목록을 만듭니다.

2. `max_abs_y = max(abs_y)` - 데이터를 정규화하기 위해 최대 절대값을 찾습니다.

3. `face_alphas = [0.2 + 0.8 * (val / max_abs_y) for val in abs_y]` - 정규화된 절대 y 값을 기반으로 0.2 에서 1.0 사이의 알파 값을 계산합니다.

4. `colors_with_alphas = list(zip(facecolors, face_alphas))` - 각 색상을 해당 알파 값과 쌍으로 묶어 (색상, 알파) 튜플 목록을 만듭니다.

5. `ax.bar(..., color=colors_with_alphas, ...)` - (색상, 알파) 튜플을 사용하여 각 막대에 대해 서로 다른 알파 값을 설정합니다.

가변적인 투명도 수준을 사용하는 이 접근 방식은 다음과 같은 경우에 효과적입니다.

- 더 중요한 데이터 포인트를 강조할 때
- 덜 중요한 데이터 포인트를 강조하지 않을 때
- 데이터 값을 기반으로 시각적 계층 구조를 만들 때
- 시각화에 추가적인 정보 차원을 추가할 때

가변적인 알파 값이 막대 높이와 불투명도 모두에 의해 데이터 포인트의 크기가 강조되는 시각적 효과를 어떻게 만드는지 명확하게 볼 수 있습니다.
