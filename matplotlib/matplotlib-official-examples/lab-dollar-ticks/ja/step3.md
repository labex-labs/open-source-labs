# Y 軸ラベルにドル記号を付けてフォーマットする

基本的なプロットができたので、Y 軸のラベルにドル記号を表示するようにフォーマットしましょう。これにより、金融データが読みやすく、よりプロフェッショナルに表示されます。

Y 軸の目盛りラベルをフォーマットするには、Matplotlib の `ticker` モジュールを使用します。このモジュールには様々なフォーマットオプションが用意されています。具体的には、`StrMethodFormatter` クラスを使って Y 軸用のカスタムフォーマッタを作成します。

ノートブックの新しいセルに以下のコードを追加して実行します。

```python
# Import the necessary module for formatting
import matplotlib.ticker as ticker

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)

# Format y-axis with dollar signs
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)

# Add labels and title
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Revenue ($)', fontsize=12)
ax.set_title('Daily Revenue Over 30 Days', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()

print("Plot with dollar-formatted y-axis created!")
```

このコードを実行すると、Y 軸のラベルにドル記号が付いた新しいプロットが表示されるはずです。

このコードの重要な部分を説明しましょう。

```python
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)
```

このフォーマット文字列の機能は次の通りです。

- `$` - 各ラベルの先頭にドル記号を追加します。
- `{x:,.2f}` - 数値を次のようにフォーマットします。
  - `,` - 千の位区切りとしてカンマを使用します（例: 1,000 は 1000 ではなく）。
  - `.2f` - 小数点以下 2 桁に丸めます（例: $1,234.56）。

このフォーマッタは Y 軸のすべての主要な目盛りラベルに適用されます。プロットが現在、値がドルであることを明確に示していることに注目してください。これにより、金融データの可視化にはるかに適したものになります。
