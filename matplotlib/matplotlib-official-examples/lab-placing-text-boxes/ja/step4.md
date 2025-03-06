# テキストボックスのカスタマイズ

グラフにテキストボックスを成功に追加したので、様々なカスタマイズオプションを探索して、視覚的に魅力的で様々なコンテキストに適したものにしましょう。

## 異なるスタイルの試行

異なるテキストボックスのスタイルを簡単に試すための関数を作成しましょう。新しいセルに以下のコードを入力して実行します。

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

この関数を使って、異なるボックススタイルを試してみましょう。新しいセルに以下を入力して実行します。

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

このセルを実行すると、それぞれ異なるテキストボックスのスタイルが適用された4つのグラフが表示されます。

## テキストボックスの位置変更

テキストボックスの位置は、ビジュアライゼーションにとって重要な要素です。グラフの異なる角にテキストボックスを配置してみましょう。新しいセルに以下を入力して実行します。

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

このコードは、それぞれ異なる角にテキストボックスが配置された2x2のヒストグラムのグリッドを作成します。

## テキストボックスの位置決めの理解

テキストボックスの位置決めを制御するいくつかの重要なパラメータがあります。

1. **位置座標**：`(x, y)` 座標は、テキストボックスが配置される場所を決定します。`transform=ax.transAxes` を使用する場合、これらは軸座標であり、`(0, 0)` は左下隅、`(1, 1)` は右上隅を表します。

2. **垂直方向の配置**：`verticalalignment` パラメータは、テキストがy座標に対して垂直方向にどのように配置されるかを制御します。

   - `'top'`：テキストの上部が指定されたy座標に位置します。
   - `'center'`：テキストの中央が指定されたy座標に位置します。
   - `'bottom'`：テキストの下部が指定されたy座標に位置します。

3. **水平方向の配置**：`horizontalalignment` パラメータは、テキストがx座標に対して水平方向にどのように配置されるかを制御します。
   - `'left'`：テキストの左側の端が指定されたx座標に位置します。
   - `'center'`：テキストの中央が指定されたx座標に位置します。
   - `'right'`：テキストの右側の端が指定されたx座標に位置します。

これらの配置オプションは、テキストを角に配置する場合に特に重要です。たとえば、右上隅にテキストを配置する場合は、`horizontalalignment='right'` を使用して、テキストの右側の端をグラフの右側の端に合わせることができます。
