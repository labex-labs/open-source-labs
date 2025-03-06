# グラフをさらにカスタマイズする

x 軸の目盛りラベルを上部に移動したので、グラフをさらにカスタマイズして、視覚的に魅力的で情報量の多いものにしましょう。

## 高度なグラフカスタマイズ手法

Matplotlib はグラフをカスタマイズするための多数のオプションを提供しています。これらのオプションのいくつかを探索しましょう。

```python
# Create a new figure and a set of axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate some data with more points for a smoother curve
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot multiple datasets
ax.plot(x, y1, linewidth=2, color='blue', label='sin(x)')
ax.plot(x, y2, linewidth=2, color='red', label='cos(x)')

# Fill the area between curves
ax.fill_between(x, y1, y2, where=(y1 > y2), alpha=0.3, color='green', interpolate=True)
ax.fill_between(x, y1, y2, where=(y1 <= y2), alpha=0.3, color='purple', interpolate=True)

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',
    top=True,
    labeltop=True,
    bottom=False,
    labelbottom=False
)

# Customize tick labels
ax.set_xticks(np.arange(0, 2*np.pi + 0.1, np.pi/2))
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

# Add title and labels with custom styles
ax.set_title('Sine and Cosine Functions with Customized X-Axis Labels at the Top',
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Angle (radians)', fontsize=12)
ax.set_ylabel('Function Value', fontsize=12)

# Add a grid and customize its appearance
ax.grid(True, linestyle='--', alpha=0.7, which='both')

# Customize the axis limits
ax.set_ylim(-1.2, 1.2)

# Add a legend with custom location and style
ax.legend(loc='upper right', fontsize=12, framealpha=0.8)

# Add annotations to highlight important points
ax.annotate('Maximum', xy=(np.pi/2, 1), xytext=(np.pi/2, 1.1),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
            fontsize=10, ha='center')

# Display the plot
plt.tight_layout()  # Adjust spacing for better appearance
plt.show()

print("We have created a fully customized plot with x-axis tick labels at the top!")
```

このコードを実行すると、以下の要素を持つ、より洗練されたプロフェッショナルな見た目のグラフが表示されます。

- 2 つの曲線（正弦波と余弦波）
- 曲線間の色付き領域
- カスタム目盛りラベル（π 表記を使用）
- 重要な特徴を指す注釈
- より良い間隔とスタイル

`tick_params()` メソッドを使って x 軸の目盛りラベルを上部に配置したまま、追加のカスタマイズでグラフを強化したことに注目してください。

## カスタマイズの理解

追加したいくつかの重要なカスタマイズを分解してみましょう。

1. `fill_between()`: 正弦波と余弦波の曲線間に色付き領域を作成します。
2. `set_xticks()` と `set_xticklabels()`: 目盛りの位置とラベルをカスタマイズします。
3. `tight_layout()`: グラフの間隔を自動的に調整して、見た目を改善します。
4. `annotate()`: 特定の点を指す矢印付きのテキストを追加します。
5. 様々な要素のフォント、色、スタイルをカスタマイズします。

これらのカスタマイズは、x 軸の目盛りラベルを上部に配置したまま、視覚的に魅力的で情報量の多いグラフを作成する方法を示しています。
