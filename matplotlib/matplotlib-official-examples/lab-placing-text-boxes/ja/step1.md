# Jupyter Notebook の作成とデータの準備

最初のステップでは、新しい Jupyter Notebook を作成し、データビジュアライゼーションのためのデータを準備します。

## 新しい Notebook の作成

Notebook の最初のセルで、必要なライブラリをインポートしましょう。以下のコードを入力し、「Run」ボタンをクリックするか、Shift+Enter キーを押して実行します。

```python
import matplotlib.pyplot as plt
import numpy as np
```

![libraries-imported](../assets/screenshot-20250306-Azb1cb3S@2x.png)

このコードは、2 つの重要なライブラリをインポートします。

- `matplotlib.pyplot`：matplotlib を MATLAB のように動作させる関数のコレクション
- `numpy`：Python における科学計算のための基本的なパッケージ

## サンプルデータの作成

次に、ビジュアライズするサンプルデータを作成しましょう。新しいセルに以下のコードを入力して実行します。

```python
# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate 10,000 random numbers from a normal distribution
x = 30 * np.random.randn(10000)

# Calculate basic statistics
mu = x.mean()
median = np.median(x)
sigma = x.std()

# Display the statistics
print(f"Mean (μ): {mu:.2f}")
print(f"Median: {median:.2f}")
print(f"Standard Deviation (σ): {sigma:.2f}")
```

このセルを実行すると、以下のような出力が表示されます。

```
Mean (μ): -0.31
Median: -0.28
Standard Deviation (σ): 29.86
```

正確な値は多少異なる場合があります。私たちは、正規分布から生成された 10,000 個の乱数を含むデータセットを作成し、3 つの重要な統計量を計算しました。

1. 平均 (μ)：すべてのデータポイントの平均値
2. 中央値：データを順番に並べたときの中央の値
3. 標準偏差 (σ)：データの分散の尺度

これらの統計量は、後でビジュアライゼーションに注釈を付けるために使用されます。
