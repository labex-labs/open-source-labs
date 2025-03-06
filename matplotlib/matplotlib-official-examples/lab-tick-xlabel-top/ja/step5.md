# グラフの保存と共有

最後のステップは、カスタマイズしたグラフを保存して、レポートやプレゼンテーションに含めたり、他の人と共有できるようにすることです。

## 様々な形式でグラフを保存する

Matplotlib を使うと、PNG、JPG、PDF、SVG など、様々な形式でグラフを保存できます。異なる形式でグラフを保存する方法を学んでみましょう。

```python
# Create a plot similar to our previous customized one
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot the data
ax.plot(x, y1, linewidth=2, color='blue', label='sin(x)')
ax.plot(x, y2, linewidth=2, color='red', label='cos(x)')

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

# Add title and labels
ax.set_title('Plot with X-Axis Labels at the Top', fontsize=14)
ax.set_xlabel('X-axis at the top')
ax.set_ylabel('Y-axis')

# Add grid and legend
ax.grid(True)
ax.legend()

# Save the figure in different formats
plt.savefig('plot_with_top_xlabels.png', dpi=300, bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.pdf', bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.svg', bbox_inches='tight')

# Show the plot
plt.show()

print("The plot has been saved in PNG, PDF, and SVG formats in the current directory.")
```

このコードを実行すると、グラフは 3 つの異なる形式で保存されます。

- PNG: ウェブや一般的な用途に適したラスター画像形式
- PDF: 出版物やレポートに最適なベクター形式
- SVG: ウェブや編集可能なグラフィックスに最適なベクター形式

ファイルは、Jupyter Notebook の現在の作業ディレクトリに保存されます。

## 保存パラメータの理解

`savefig()` で使用されるパラメータを見てみましょう。

- `dpi=300`: PNG などのラスター形式の解像度（1 インチあたりのドット数）を設定します。
- `bbox_inches='tight'`: 不要な余白をなくし、すべての要素を含むように図の境界を自動的に調整します。

## 保存したファイルを表示する

保存したファイルは、Jupyter のファイルブラウザを使って表示できます。

1. 左上の「Jupyter」ロゴをクリックします。
2. ファイルブラウザで、保存された画像ファイルが表示されます。
3. 任意のファイルをクリックして、表示またはダウンロードします。

## 追加のグラフエクスポートオプション

保存するグラフをより細かく制御するには、図のサイズをカスタマイズしたり、背景を調整したり、必要に応じて DPI を変更したりできます。

```python
# Control the background color and transparency
fig.patch.set_facecolor('white')  # Set figure background color
fig.patch.set_alpha(0.8)          # Set background transparency

# Save with custom settings
plt.savefig('custom_background_plot.png',
            dpi=400,              # Higher resolution
            facecolor=fig.get_facecolor(),  # Use the figure's background color
            edgecolor='none',     # No edge color
            bbox_inches='tight',  # Tight layout
            pad_inches=0.1)       # Add a small padding

print("A customized plot has been saved with specialized export settings.")
```

これは、出力形式と外観を精密に制御してグラフを保存する方法を示しています。
