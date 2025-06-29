# 異なるアルファ手法を用いた複合可視化の作成

この最後のステップでは、複数の手法を組み合わせて、1 つのプロット内で均一なアルファ値と異なるアルファ値の両方を示す、より複雑な可視化を作成します。

## 新しいセルの追加

ツールバーの「+」ボタンをクリックするか、コマンドモードで「Esc」を押してから「b」を押すことで、Jupyter Notebook に新しいセルを追加します。

## 複合可視化の作成

新しいセルに以下のコードを入力して実行します。

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Generate some common data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# First subplot: Fixed alpha for all lines
ax1.plot(x, y1, color='red', linewidth=2, label='sin(x)', alpha=0.7)
ax1.plot(x, y2, color='blue', linewidth=2, label='cos(x)', alpha=0.7)
ax1.plot(x, y3, color='green', linewidth=2, label='sin(x)cos(x)', alpha=0.7)

# Add title and legend to first subplot
ax1.set_title("Multiple Lines with Uniform Alpha")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.5)

# Second subplot: Scatter plot with varying alpha based on y-value
sizes = np.abs(y3 * 100) + 10  # Vary point sizes based on y3
colors = y3  # Use y3 values for coloring

# Calculate varying alpha values between 0.3 and 1.0 based on absolute y3 values
alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))

# Create a scatter plot with varying sizes, colors, and alphas
scatter = ax2.scatter(x, y3, s=sizes, c=colors, cmap='viridis',
                     alpha=alphas)

# Add title and labels to second subplot
ax2.set_title("Scatter Plot with Varying Alpha Based on Y-Value")
ax2.set_xlabel("x")
ax2.set_ylabel("sin(x)cos(x)")
ax2.grid(True, linestyle='--', alpha=0.5)

# Add a colorbar to the second subplot
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Value of sin(x)cos(x)')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
```

## コードと出力の理解

コードを実行すると、横並びの 2 つのサブプロットがあるグラフが表示されるはずです。

1. **左のサブプロット（均一なアルファ）**：同じアルファ値（0.7）でプロットされた 3 つの三角関数を示します。

2. **右のサブプロット（異なるアルファ）**：散布図を示し、以下の通りです。
   - x 座標は入力値です。
   - y 座標は sin(x)cos(x) です。
   - 各点のサイズは絶対 y 値に基づいて変化します。
   - 各点の色は y 値に基づいて変化します。
   - 各点のアルファ（透明度）は絶対 y 値に基づいて変化します。

コードの重要な部分を分析してみましょう。

1. `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))` - 横並びの 2 つのサブプロットを持つグラフを作成します。

2. 最初のサブプロットについて：
   - `ax1.plot(..., alpha=0.7)` - 3 つの線すべてに均一なアルファ値を使用します。

3. 2 番目のサブプロットについて：
   - `alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))` - 0.3 から 1.0 の間の異なるアルファ値を計算します。
   - `ax2.scatter(..., alpha=alphas)` - 散布点に異なるアルファ値を使用します。

これらの手法の組み合わせは、アルファ値が可視化を強化するために様々な方法で使用できることを示しています。

- **均一なアルファ**：同等の重要性を持つ複数の重複要素を表示する必要がある場合に役立ちます。

- **異なるアルファ**：特定のデータポイントをその値に基づいて強調したい場合に役立ちます。

これらの手法を習得することで、より効果的で視覚的に魅力的なデータ可視化を作成することができます。
