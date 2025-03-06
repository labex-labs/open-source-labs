# 画像オーバーレイ用の再利用可能な関数の作成

コードをより再利用可能にするために、Matplotlib の任意の図に画像をオーバーレイできる関数を作成しましょう。これにより、異なるグラフに同じ効果を簡単に適用できます。

1. Notebook で新しいセルを作成し、以下のコードを入力します。

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

このコードは `add_image_overlay` という関数を定義しています。この関数は以下のことを行います。

- 図、画像のパス、位置、透明度、z オーダーのパラメータを受け取ります。
- 指定された画像を読み込みます。
- `figimage` を使用して画像を図に追加します。
- 変更された図を返します。

関数を定義した後、ランダムデータの散布図を作成し、Matplotlib のロゴをオーバーレイすることで、その使用方法を示しています。

2. Shift + Enter を押してセルを実行します。

出力には、ランダムに配置された色付きの点からなる散布図が表示され、位置 (50, 50) に 40% の不透明度で Matplotlib のロゴがオーバーレイされているはずです。

3. 折れ線グラフを使ったもう 1 つの例を試してみましょう。新しいセルを作成し、以下のコードを入力します。

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

このコードは正弦波を示す折れ線グラフを作成し、グラフの右下隅に Matplotlib のロゴを追加します。

4. Shift + Enter を押してセルを実行します。

出力には、正弦波の折れ線グラフが表示され、右下隅に 60% の不透明度で Matplotlib のロゴがオーバーレイされているはずです。

これらの例は、`add_image_overlay` 関数を使用して異なるタイプのグラフに簡単に画像をオーバーレイできることを示しており、ビジュアライゼーションをカスタマイズするための汎用的なツールとなっています。
