# 텍스트 상자 사용자 정의

이제 플롯에 텍스트 상자를 성공적으로 추가했으므로 시각적으로 더 매력적이고 다양한 상황에 적합하도록 다양한 사용자 정의 옵션을 살펴보겠습니다.

## 다양한 스타일 실험

다양한 텍스트 상자 스타일을 더 쉽게 실험할 수 있도록 함수를 만들어 보겠습니다. 새 셀에 다음 코드를 입력하고 실행합니다.

```python
def plot_with_textbox(boxstyle, facecolor, alpha, position=(0.05, 0.95)):
    """
    Create a histogram with a custom text box.

    Parameters:
    boxstyle (str): Style of the box ('round', 'square', 'round4', etc.)
    facecolor (str): Background color of the box
    alpha (float): Transparency of the box (0-1)
    position (tuple): Position of the box in axes coordinates (x, y)
    """
    # Create figure and plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(x, bins=50, color='skyblue', edgecolor='black')

    # Set title and labels
    ax.set_title(f'Text Box Style: {boxstyle}', fontsize=16)
    ax.set_xlabel('Value', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)

    # Create text box properties
    box_props = dict(boxstyle=boxstyle, facecolor=facecolor, alpha=alpha)

    # Add text box
    ax.text(position[0], position[1], textstr, transform=ax.transAxes,
            fontsize=14, verticalalignment='top', bbox=box_props)

    plt.tight_layout()
    plt.show()
```

이제 이 함수를 사용하여 다양한 상자 스타일을 시도해 보겠습니다. 새 셀에 다음을 입력하고 실행합니다.

```python
# Try a square box with light green color
plot_with_textbox('square', 'lightgreen', 0.7)

# Try a rounded box with light blue color
plot_with_textbox('round', 'lightblue', 0.5)

# Try a box with extra rounded corners
plot_with_textbox('round4', 'lightyellow', 0.6)

# Try a sawtooth style box
plot_with_textbox('sawtooth', 'lightcoral', 0.4)
```

이 셀을 실행하면 각기 다른 텍스트 상자 스타일이 있는 네 개의 서로 다른 플롯이 표시됩니다.

## 텍스트 상자 위치 변경

텍스트 상자의 위치는 시각화에 매우 중요할 수 있습니다. 플롯의 다른 모서리에 텍스트 상자를 배치해 보겠습니다. 새 셀에 다음을 입력하고 실행합니다.

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()  # Flatten to easily iterate

# Define positions for the four corners
positions = [
    (0.05, 0.95),  # Top left
    (0.95, 0.95),  # Top right
    (0.05, 0.05),  # Bottom left
    (0.95, 0.05)   # Bottom right
]

# Define alignments for each position
alignments = [
    ('top', 'left'),          # Top left
    ('top', 'right'),         # Top right
    ('bottom', 'left'),       # Bottom left
    ('bottom', 'right')       # Bottom right
]

# Corner labels
corner_labels = ['Top Left', 'Top Right', 'Bottom Left', 'Bottom Right']

# Create four plots with text boxes in different corners
for i, ax in enumerate(axes):
    # Plot histogram
    ax.hist(x, bins=50, color='skyblue', edgecolor='black')

    # Set title
    ax.set_title(f'Text Box in {corner_labels[i]}', fontsize=14)

    # Create text box properties
    box_props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    # Add text box
    ax.text(positions[i][0], positions[i][1], textstr,
            transform=ax.transAxes, fontsize=12,
            verticalalignment=alignments[i][0],
            horizontalalignment=alignments[i][1],
            bbox=box_props)

plt.tight_layout()
plt.show()
```

이 코드는 각기 다른 모서리에 텍스트 상자가 있는 2x2 그리드의 히스토그램을 생성합니다.

## 텍스트 상자 위치 지정 이해

텍스트 상자 위치를 제어하는 몇 가지 주요 매개변수가 있습니다.

1. **위치 좌표**: `(x, y)` 좌표는 텍스트 상자가 배치되는 위치를 결정합니다. `transform=ax.transAxes`를 사용하는 경우, 이는 `(0, 0)`이 왼쪽 하단 모서리이고 `(1, 1)`이 오른쪽 상단 모서리인 축 좌표입니다.

2. **수직 정렬**: `verticalalignment` 매개변수는 텍스트가 y 좌표를 기준으로 수직으로 정렬되는 방식을 제어합니다.

   - `'top'`: 텍스트의 맨 위가 지정된 y 좌표에 있습니다.
   - `'center'`: 텍스트의 중심이 지정된 y 좌표에 있습니다.
   - `'bottom'`: 텍스트의 맨 아래가 지정된 y 좌표에 있습니다.

3. **수평 정렬**: `horizontalalignment` 매개변수는 텍스트가 x 좌표를 기준으로 수평으로 정렬되는 방식을 제어합니다.
   - `'left'`: 텍스트의 왼쪽 가장자리가 지정된 x 좌표에 있습니다.
   - `'center'`: 텍스트의 중심이 지정된 x 좌표에 있습니다.
   - `'right'`: 텍스트의 오른쪽 가장자리가 지정된 x 좌표에 있습니다.

이러한 정렬 옵션은 모서리에 텍스트를 배치할 때 특히 중요합니다. 예를 들어, 오른쪽 상단 모서리에서는 `horizontalalignment='right'`를 사용하여 텍스트의 오른쪽 가장자리가 플롯의 오른쪽 가장자리에 정렬되도록 합니다.
