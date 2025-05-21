# 다양한 알파 기술을 사용한 결합된 시각화 만들기

이 마지막 단계에서는 여러 기술을 결합하여 하나의 플롯에서 균일하고 가변적인 알파 값을 모두 보여주는 보다 복잡한 시각화를 만듭니다.

## 새 셀 추가

도구 모음에서 "+" 버튼을 클릭하거나 명령 모드에서 "Esc"를 누른 다음 "b"를 눌러 Jupyter Notebook 에 새 셀을 추가합니다.

## 결합된 시각화 만들기

새 셀에 다음 코드를 입력하고 실행합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Generate some common data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# First subplot: Fixed alpha for all lines
ax1.plot(x, y1, color='red', linewidth=2, label='sin(x)', alpha=0.7)
ax1.plot(x, y2, color='blue', linewidth=2, label='cos(x)', alpha=0.7)
ax1.plot(x, y3, color='green', linewidth=2, label='sin(x)cos(x)', alpha=0.7)

# Add title and legend to first subplot
ax1.set_title("Multiple Lines with Uniform Alpha")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.5)

# Second subplot: Scatter plot with varying alpha based on y-value
sizes = np.abs(y3 * 100) + 10  # Vary point sizes based on y3
colors = y3  # Use y3 values for coloring

# Calculate varying alpha values between 0.3 and 1.0 based on absolute y3 values
alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))

# Create a scatter plot with varying sizes, colors, and alphas
scatter = ax2.scatter(x, y3, s=sizes, c=colors, cmap='viridis',
                     alpha=alphas)

# Add title and labels to second subplot
ax2.set_title("Scatter Plot with Varying Alpha Based on Y-Value")
ax2.set_xlabel("x")
ax2.set_ylabel("sin(x)cos(x)")
ax2.grid(True, linestyle='--', alpha=0.5)

# Add a colorbar to the second subplot
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Value of sin(x)cos(x)')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
```

## 코드 및 출력 이해하기

코드를 실행한 후 두 개의 서브플롯이 나란히 있는 그림이 표시되어야 합니다.

1. **왼쪽 서브플롯 (균일한 알파)**: 동일한 알파 값 (0.7) 으로 플로팅된 세 개의 삼각 함수를 보여줍니다.

2. **오른쪽 서브플롯 (가변적인 알파)**: 다음을 보여주는 산점도입니다.
   - x 좌표는 입력 값입니다.
   - y 좌표는 sin(x)cos(x) 입니다.
   - 각 점의 크기는 절대 y 값을 기준으로 달라집니다.
   - 각 점의 색상은 y 값을 기준으로 달라집니다.
   - 각 점의 알파 (투명도) 는 절대 y 값을 기준으로 달라집니다.

코드의 주요 부분을 분석해 보겠습니다.

1. `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))` - 두 개의 나란한 서브플롯이 있는 그림을 만듭니다.

2. 첫 번째 서브플롯의 경우:

   - `ax1.plot(..., alpha=0.7)` - 세 개의 모든 선에 대해 균일한 알파 값을 사용합니다.

3. 두 번째 서브플롯의 경우:
   - `alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))` - 0.3 에서 1.0 사이의 가변적인 알파 값을 계산합니다.
   - `ax2.scatter(..., alpha=alphas)` - 산점도에 가변적인 알파 값을 사용합니다.

이러한 기술의 조합은 알파 값을 다양한 방식으로 사용하여 시각화를 향상시키는 방법을 보여줍니다.

- **균일한 알파**는 동일한 중요도로 여러 겹치는 요소를 표시해야 할 때 도움이 됩니다.

- **가변적인 알파**는 값에 따라 특정 데이터 포인트를 강조하려는 경우 도움이 됩니다.

이러한 기술을 마스터하면 보다 효과적이고 시각적으로 매력적인 데이터 시각화를 만들 수 있습니다.
