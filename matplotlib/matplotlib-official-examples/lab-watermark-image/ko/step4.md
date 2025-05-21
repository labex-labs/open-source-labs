# 플롯에 이미지 오버레이

이제 기본 플롯을 만들었으므로 이미지를 오버레이해 보겠습니다. `figimage` 메서드를 사용하여 그림에 이미지를 추가하고, 아래의 플롯이 계속 보이도록 반투명하게 만들 것입니다.

1. 노트북에 새 셀을 만들고 다음 코드를 입력합니다.

```python
# Create a figure and axes for our plot (same as before)
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)  # x-axis values (0 to 29)
y = x + np.random.randn(30)  # y-axis values (x plus random noise)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')  # Green bars

# Add grid lines
ax.grid(linestyle='--', alpha=0.7)

# Add labels and title
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Image Overlay')

# Load the image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Overlay the image on the plot
# Parameters:
# - im: the image data
# - 25, 25: x and y position in pixels from the bottom left
# - zorder=3: controls the drawing order (higher numbers are drawn on top)
# - alpha=0.5: controls the transparency (0 = transparent, 1 = opaque)
fig.figimage(im, 25, 25, zorder=3, alpha=0.5)

# Display the plot
plt.tight_layout()
plt.show()
```

이 코드는 이전 단계에서 수행한 작업을 결합하고 `figimage` 메서드를 추가하여 플롯에 이미지를 오버레이합니다. `figimage` 매개변수에 대한 설명은 다음과 같습니다.

- `im`: NumPy 배열로 된 이미지 데이터.
- `25, 25`: 그림의 왼쪽 하단 모서리에서 픽셀 단위의 x 및 y 위치.
- `zorder=3`: 그리기 순서를 제어합니다. 숫자가 높을수록 숫자가 낮은 요소 위에 그려집니다.
- `alpha=0.5`: 이미지의 투명도를 제어합니다. 값 0 은 완전히 투명하고 1 은 완전히 불투명합니다.

2. Shift+Enter 를 눌러 셀을 실행합니다.

출력은 이전과 동일한 막대 차트를 표시하지만 이제 Matplotlib 로고가 왼쪽 하단 모서리에 오버레이됩니다. 로고는 반투명하여 아래의 플롯이 계속 보이도록 합니다.

3. 다양한 위치와 투명도 수준을 실험해 보겠습니다. 새 셀을 만들고 다음 코드를 입력합니다.

```python
# Create a figure and axes for our plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)
y = x + np.random.randn(30)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Centered Image Overlay')

# Load the image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Get figure dimensions
fig_width, fig_height = fig.get_size_inches() * fig.dpi

# Calculate center position (this is approximate)
x_center = fig_width / 2 - im.shape[1] / 2
y_center = fig_height / 2 - im.shape[0] / 2

# Overlay the image at the center with higher transparency
fig.figimage(im, x_center, y_center, zorder=3, alpha=0.3)

# Display the plot
plt.tight_layout()
plt.show()
```

이 코드는 이미지를 그림의 중앙에 배치하고 투명도 수준을 높여 (alpha=0.3) 워터마크로 사용하기에 더 적합하게 만듭니다.

4. Shift+Enter 를 눌러 셀을 실행합니다.

출력은 이전보다 더 투명한 로고가 중앙에 배치된 막대 차트를 표시하여 워터마크 효과를 만듭니다.
