# アルファ値を使用した散布図の作成

このステップでは、アルファ値に関する知識を活用して散布図を作成します。これにより、透明度が重複する点を持つ散布図におけるデータの密度を可視化するのにどのように役立つかを示します。

## 新しいセルの追加

ツールバーの「+」ボタンをクリックするか、コマンドモードで「Esc」を押してから「b」を押すことで、Jupyter Notebook に新しいセルを追加します。

## 透明度を持つ散布図の作成

新しいセルに以下のコードを入力して実行します。

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create two clusters of points
cluster1_x = np.random.normal(0.3, 0.15, 500)
cluster1_y = np.random.normal(0.3, 0.15, 500)

cluster2_x = np.random.normal(0.7, 0.15, 500)
cluster2_y = np.random.normal(0.7, 0.15, 500)

# Combine the clusters
x = np.concatenate([cluster1_x, cluster2_x])
y = np.concatenate([cluster1_y, cluster2_y])

# Create a scatter plot with alpha=0.5
scatter = ax.scatter(x, y, s=30, c='blue', alpha=0.5)

# Add a title and labels
ax.set_title("Scatter Plot with Alpha=0.5 Showing Data Density")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Set axis limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Add a grid
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## コードと出力の理解

コードを実行すると、2 つの点のクラスターがある散布図が表示されるはずです。各点の透明度レベルは 0.5 で、点が重複する部分を見ることができます。

コードの重要な部分を分解してみましょう。

1. `cluster1_x = np.random.normal(0.3, 0.15, 500)` - 平均 0.3、標準偏差 0.15 の正規分布に従って 500 個のランダムな x 座標を生成します。

2. `cluster1_y = np.random.normal(0.3, 0.15, 500)` - 最初のクラスターの 500 個のランダムな y 座標を生成します。

3. `cluster2_x` と `cluster2_y` - 同様に、(0.7, 0.7) を中心とする 2 番目のクラスターの座標を生成します。

4. `ax.scatter(..., alpha=0.5)` - 点の不透明度が 50% の散布図を作成します。

散布図でアルファを使用する利点は以下の通りです。

1. **密度の可視化**：多くの点が重複する領域は暗く表示され、データの密度がわかります。

2. **重複プロットの軽減**：透明度がない場合、重複する点は完全に互いを隠してしまいます。

3. **パターンの認識**：透明度は、データ内のクラスターやパターンを識別するのに役立ちます。

可視化では、より多くの点が重複する領域が暗く表示されることに注目してください。これは、密度推定のような追加の手法を必要とせずにデータの密度を可視化する強力な方法です。
