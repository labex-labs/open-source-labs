# Matplotlib でのアルファ値の理解

この最初のステップでは、Jupyter Notebook を作成し、アルファ値を使用した基本的な可視化の設定方法を学びます。

## 最初の Jupyter Notebook セルの作成

このセルでは、必要なライブラリをインポートし、異なるアルファ値を持つ 2 つの重なり合う円を作成して、透明度を実証します。

```python
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(6, 4))

# Create a circle with alpha=1.0 (completely opaque)
circle1 = plt.Circle((0.5, 0.5), 0.3, color='blue', alpha=1.0, label='Opaque (alpha=1.0)')

# Create a circle with alpha=0.5 (semi-transparent)
circle2 = plt.Circle((0.7, 0.5), 0.3, color='red', alpha=0.5, label='Semi-transparent (alpha=0.5)')

# Add circles to the axes
ax.add_patch(circle1)
ax.add_patch(circle2)

# Set axis limits
ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1)

# Add a title and legend
ax.set_title('Demonstrating Alpha Values in Matplotlib')
ax.legend(loc='upper right')

# Show the plot
plt.show()
```

このコードをセルに入力したら、Shift+Enter を押すか、ツールバーの「Run」ボタンをクリックして実行します。

## 出力の理解

重なり合う 2 つの円が表示されるはずです。

- 左の青い円は完全に不透明です（アルファ = 1.0）
- 右の赤い円は半透明です（アルファ = 0.5）

重なっている部分で赤い円を通して青い円が見えることに注目してください。これは、赤い円のアルファ値を 0.5 に設定した効果です。

アルファ値は可視化の透明度を制御し、以下の場合に役立ちます。

- 重なり合うデータポイントを表示するとき
- 特定の要素を強調するとき
- 密集したプロットの視覚的な混乱を減らすとき
- レイヤードな可視化を作成するとき

次のステップでは、アルファ値のさらなる応用例を探索しましょう。
