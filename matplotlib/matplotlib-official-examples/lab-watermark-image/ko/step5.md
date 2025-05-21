# 이미지 오버레이를 위한 재사용 가능한 함수 생성

코드를 더 재사용 가능하게 만들기 위해, 모든 Matplotlib figure 에 이미지 오버레이를 추가할 수 있는 함수를 만들어 보겠습니다. 이렇게 하면 동일한 효과를 다양한 플롯에 쉽게 적용할 수 있습니다.

1. 노트북에 새 셀을 만들고 다음 코드를 입력합니다.

```python
def add_image_overlay(fig, image_path, x_pos=25, y_pos=25, alpha=0.5, zorder=3):
    """
    Add an image overlay to a matplotlib figure.

    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        The figure to add the image to
    image_path : str
        Path to the image file
    x_pos : int
        X position in pixels from the bottom left
    y_pos : int
        Y position in pixels from the bottom left
    alpha : float
        Transparency level (0 to 1)
    zorder : int
        Drawing order (higher numbers are drawn on top)

    Returns:
    --------
    fig : matplotlib.figure.Figure
        The figure with the image overlay
    """
    # Load the image
    with cbook.get_sample_data(image_path) as file:
        im = image.imread(file)

    # Add the image to the figure
    fig.figimage(im, x_pos, y_pos, zorder=zorder, alpha=alpha)

    return fig

# Example usage: Create a scatter plot with an image overlay
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data for a scatter plot
x = np.random.rand(50) * 10
y = np.random.rand(50) * 10

# Create a scatter plot
ax.scatter(x, y, s=100, c=np.random.rand(50), cmap='viridis', alpha=0.7)
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Scatter Plot with Image Overlay')

# Add the image overlay using our function
add_image_overlay(fig, 'logo2.png', x_pos=50, y_pos=50, alpha=0.4)

# Display the plot
plt.tight_layout()
plt.show()
```

이 코드는 `add_image_overlay`라는 함수를 정의합니다. 이 함수는 다음과 같은 기능을 수행합니다.

- figure, 이미지 경로, 위치, 투명도 및 z-order 에 대한 매개변수를 사용합니다.
- 지정된 이미지를 로드합니다.
- `figimage`를 사용하여 이미지를 figure 에 추가합니다.
- 수정된 figure 를 반환합니다.

함수를 정의한 후, 임의 데이터를 사용하여 산점도를 만들고 Matplotlib 로고를 오버레이로 추가하여 사용법을 시연합니다.

2. Shift+Enter 를 눌러 셀을 실행합니다.

출력은 임의로 배치되고 색상이 지정된 점이 있는 산점도와 40% 불투명도로 위치 (50, 50) 에 오버레이된 Matplotlib 로고를 표시해야 합니다.

3. 선 그래프로 예제를 하나 더 시도해 보겠습니다. 새 셀을 만들고 다음 코드를 입력합니다.

```python
# Example usage: Create a line plot with an image overlay
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data for a line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line plot
ax.plot(x, y, linewidth=2, color='#d62728')
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Sine Wave with Image Overlay')
ax.set_ylim(-1.5, 1.5)

# Add the image overlay using our function
# Place it in the bottom right corner
fig_width, fig_height = fig.get_size_inches() * fig.dpi
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)
    x_pos = fig_width - im.shape[1] - 50  # 50 pixels from the right edge

add_image_overlay(fig, 'logo2.png', x_pos=x_pos, y_pos=50, alpha=0.6)

# Display the plot
plt.tight_layout()
plt.show()
```

이 코드는 사인파를 보여주는 선 그래프를 만들고, 플롯의 오른쪽 하단 모서리에 Matplotlib 로고를 추가합니다.

4. Shift+Enter 를 눌러 셀을 실행합니다.

출력은 60% 불투명도로 오른쪽 하단 모서리에 Matplotlib 로고가 오버레이된 사인파의 선 그래프를 표시해야 합니다.

이러한 예제는 `add_image_overlay` 함수를 사용하여 다양한 유형의 플롯에 이미지 오버레이를 쉽게 추가하여 시각화를 사용자 정의하는 데 유용한 도구임을 보여줍니다.
