# デフォルト設定で基本的なグラフを作成する

Matplotlib をインポートしたので、デフォルト設定で簡単なグラフを作成し、軸と目盛りラベルがデフォルトでどのように配置されるかを理解しましょう。

## Matplotlib のコンポーネントを理解する

Matplotlib では、グラフはいくつかのコンポーネントで構成されています。

- **Figure（図）**: グラフ全体のコンテナ
- **Axes（軸領域）**: 独自の座標系でデータがプロットされる領域
- **Axis（軸）**: 座標系を定義する数直線のようなオブジェクト
- **Ticks（目盛り）**: 特定の値を示す軸上の目印
- **Tick Labels（目盛りラベル）**: 各目盛りの値を示すテキストラベル

デフォルトでは、x 軸の目盛りラベルはグラフの下部に表示されます。

## 簡単なグラフを作成する

ノートブックの新しいセルで、簡単な折れ線グラフを作成しましょう。

```python
# Create a figure and a set of axes
fig, ax = plt.subplots(figsize=(8, 5))

# Generate some data
x = np.arange(0, 10, 1)
y = np.sin(x)

# Plot the data
ax.plot(x, y, marker='o', linestyle='-', color='blue', label='sin(x)')

# Add a title and labels
ax.set_title('A Simple Sine Wave Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis (sin(x))')

# Add a grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display the plot
plt.show()

print("Notice that the x-axis tick labels are at the bottom of the plot by default.")
```

このコードを実行すると、x 軸の目盛りラベルがグラフの下部にある正弦波のグラフが表示されます。これは Matplotlib のデフォルトの位置です。

グラフの構造や目盛りラベルの配置をしばらく観察してみましょう。この理解は、次のステップで行う変更を理解するのに役立ちます。
