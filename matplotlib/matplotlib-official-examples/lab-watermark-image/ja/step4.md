# グラフ上に画像をオーバーレイする

これでベースとなるグラフが作成できたので、その上に画像をオーバーレイしましょう。`figimage` メソッドを使用して画像を図に追加し、下のグラフが見えるように半透明にします。

1. Notebook で新しいセルを作成し、以下のコードを入力します。

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

このコードは前のステップで行ったことを組み合わせ、`figimage` メソッドを追加して画像をグラフ上にオーバーレイします。`figimage` のパラメータを以下に分解します。

- `im`: NumPy 配列としての画像データ。
- `25, 25`: 図の左下角からのピクセル単位の x と y の位置。
- `zorder=3`: 描画順序を制御します。数値が大きいほど、数値が小さい要素の上に描画されます。
- `alpha=0.5`: 画像の透明度を制御します。0 は完全に透明、1 は完全に不透明です。

2. Shift + Enter を押してセルを実行します。

出力には前と同じ棒グラフが表示され、左下隅に Matplotlib のロゴがオーバーレイされているはずです。ロゴは半透明になっており、下のグラフが見えるようになっています。

3. 異なる位置と透明度レベルで実験してみましょう。新しいセルを作成し、以下のコードを入力します。

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

このコードは、画像を図の中央に配置し、透明度レベルを高く（alpha=0.3）して、透かしとしてより適したものにします。

4. Shift + Enter を押してセルを実行します。

出力には、ロゴが中央に配置され、前よりも透明になった棒グラフが表示され、透かし効果が得られます。
