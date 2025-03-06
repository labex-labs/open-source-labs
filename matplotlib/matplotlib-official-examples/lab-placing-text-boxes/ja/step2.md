# 基本的なヒストグラムの作成

データが用意できたので、その分布を可視化するためのヒストグラムを作成しましょう。ヒストグラムはデータをビン（範囲）に分割し、各ビン内のデータポイントの頻度を示します。

## ヒストグラムの作成

Jupyter Notebookの新しいセルに以下のコードを入力して実行します。

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()
```

このセルを実行すると、ランダムデータの分布を示すヒストグラムが表示されます。出力はゼロ付近を中心とした釣鐘型の曲線（正規分布）のように見えます。

## コードの理解

コードの各行が何をするかを分解してみましょう。

1. `fig, ax = plt.subplots(figsize=(10, 6))`：グラフと軸のオブジェクトを作成します。`figsize` パラメータはグラフのサイズをインチ（幅、高さ）で設定します。

2. `histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')`：データ `x` のヒストグラムを50のビンで作成します。ビンは黒い枠線の水色に着色されます。

3. `ax.set_title('Distribution of Random Data', fontsize=16)`：フォントサイズ16のタイトルをグラフに追加します。

4. `ax.set_xlabel('Value', fontsize=12)` と `ax.set_ylabel('Frequency', fontsize=12)`：フォントサイズ12のラベルをx軸とy軸に追加します。

5. `plt.tight_layout()`：グラフを自動的に調整して図の領域に収めます。

6. `plt.show()`：グラフを表示します。

ヒストグラムはデータの分布を示しています。`np.random.randn()` を使用して正規分布からデータを生成したため、ヒストグラムは0を中心とした釣鐘型になっています。各棒の高さはその範囲内に含まれるデータポイントの数を表しています。
