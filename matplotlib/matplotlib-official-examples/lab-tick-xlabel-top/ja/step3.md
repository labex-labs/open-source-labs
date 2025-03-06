# X 軸の目盛りラベルを上部に移動する

目盛りラベルのデフォルトの配置を理解したので、x 軸の目盛りラベルをグラフの上部に移動しましょう。

## 目盛りパラメータを理解する

Matplotlib は `tick_params()` メソッドを提供しており、これを使って目盛りと目盛りラベルの表示を制御できます。このメソッドを使うと以下のことができます。

- 目盛りと目盛りラベルの表示/非表示を切り替える
- それらの位置（上部、下部、左部、右部）を変更する
- サイズ、色、その他のプロパティを調整する

## X 軸の目盛りラベルを上部に配置したグラフを作成する

x 軸の目盛りラベルを上部に移動した新しいグラフを作成しましょう。

```python
# Create a new figure and a set of axes
fig, ax = plt.subplots(figsize=(8, 5))

# Generate some data
x = np.arange(0, 10, 1)
y = np.cos(x)

# Plot the data
ax.plot(x, y, marker='s', linestyle='-', color='green', label='cos(x)')

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',         # Apply changes to the x-axis
    top=True,         # Show ticks on the top side
    labeltop=True,    # Show tick labels on the top side
    bottom=False,     # Hide ticks on the bottom side
    labelbottom=False # Hide tick labels on the bottom side
)

# Add a title and labels
ax.set_title('Cosine Wave with X-Axis Tick Labels at the Top')
ax.set_xlabel('X-axis (now at the top!)')
ax.set_ylabel('Y-axis (cos(x))')

# Add a grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display the plot
plt.show()

print("Now the x-axis tick labels are at the top of the plot!")
```

このコードを実行すると、x 軸の目盛りラベルがグラフの上部にある余弦波のグラフが表示されます。

`tick_params()` メソッドがいくつかのパラメータとともにどのように使われているかに注目してください。

- `axis='x'`: x 軸を変更することを指定します。
- `top=True` と `labeltop=True`: 上部に目盛りとラベルを表示します。
- `bottom=False` と `labelbottom=False`: 下部の目盛りとラベルを非表示にします。

これにより、x 軸のラベルが下部ではなく上部に配置された、きれいなデータの表示が得られます。
