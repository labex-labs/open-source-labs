# ランダムデータを使用した基本的なグラフの作成

画像をオーバーレイする前に、ビジュアライゼーションのベースとなるグラフを作成する必要があります。ランダムデータを使用して簡単な棒グラフを作成しましょう。

1. Notebook で新しいセルを作成し、以下のコードを入力します。

```python
# Create a figure and axes for our plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)  # x-axis values (0 to 29)
y = x + np.random.randn(30)  # y-axis values (x plus random noise)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')  # Green bars

# Add grid lines
ax.grid(linestyle='--', alpha=0.7)

# Add labels and title
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Random Data')

# Display the plot
plt.tight_layout()
plt.show()
```

このコードは以下のことを行います。

- `plt.subplots()` を使用して特定のサイズの図と軸を作成します。
- コードを実行するたびに同じランダム値が得られるように、乱数のシードを設定します。
- 30 個の x 値（0 から 29）と対応する y 値（x にランダムノイズを加えたもの）を生成します。
- `ax.bar()` を使用して緑色の棒グラフを作成します。
- `ax.grid()` を使用してグラフにグリッド線を追加します。
- x 軸、y 軸のラベルとグラフのタイトルを追加します。
- `plt.tight_layout()` を使用して余白を調整し、見栄えを良くします。
- `plt.show()` を使用してグラフを表示します。

2. Shift + Enter を押してセルを実行します。

出力には、ランダムデータを表す緑色の棒グラフが表示されるはずです。x 軸には 0 から 29 の整数が表示され、y 軸にはランダムノイズが加えられた対応する値が表示されます。

このグラフは、次のステップで画像をオーバーレイする基盤となります。図オブジェクトを変数 `fig` に、軸オブジェクトを変数 `ax` に格納したことに注意してください。これらの変数は画像をオーバーレイする際に必要になります。
