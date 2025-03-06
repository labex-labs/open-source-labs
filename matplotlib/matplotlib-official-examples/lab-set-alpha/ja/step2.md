# 均一なアルファ値の棒グラフの作成

このステップでは、`alpha` キーワード引数を使用して、すべての棒が同じ透明度レベルを持つ棒グラフを作成します。

## 新しいセルの追加

ツールバーの「+」ボタンをクリックするか、コマンドモードで「Esc」を押してから「b」を押すことで、Jupyter Notebook に新しいセルを追加します。

## 均一なアルファ値の棒グラフの作成

新しいセルに以下のコードを入力して実行します。

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Create the bar chart with alpha=0.5 for all bars
ax.bar(x_values, y_values, color=facecolors, edgecolor=edgecolors, alpha=0.5)

# Add a title and labels
ax.set_title("Bar Chart with Uniform Alpha Value (alpha=0.5)")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## コードと出力の理解

コードを実行すると、20 本の棒からなる棒グラフが表示されるはずです。各棒は、同じ透明度レベル（アルファ = 0.5）で、y 値が正の場合は緑、負の場合は赤になっています。

重要な部分を分解してみましょう。

1. `np.random.seed(19680801)` - これにより、コードを実行するたびに生成される乱数が同じになります。

2. `x_values = list(range(20))` - x 軸に 0 から 19 までの整数のリストを作成します。

3. `y_values = np.random.randn(20)` - y 軸に標準正規分布から 20 個の乱数を生成します。

4. `facecolors = ['green' if y > 0 else 'red' for y in y_values]` - このリスト内包表記により、正の値には緑、負の値には赤が割り当てられます。

5. `ax.bar(..., alpha=0.5)` - すべての棒に均一なアルファ値 0.5 を設定する重要な部分です。

均一なアルファ値により、すべての棒が同じ透明度になります。これは、以下の場合に役立ちます。

- 棒の背後にあるグリッド線を表示する
- より控えめな可視化を作成する
- すべての要素の視覚的な支配力を均等に減らす

次のステップでは、異なる棒に異なるアルファ値を設定する方法を探索します。
