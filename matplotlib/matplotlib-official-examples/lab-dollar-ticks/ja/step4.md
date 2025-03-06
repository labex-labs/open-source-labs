# 金融データの可視化を向上させるためのプロットの強化

基本的な通貨フォーマットが整ったので、金融データ分析により役立つようにプロットをさらに強化しましょう。いくつかの改良点を追加します。

1. 日平均収益を示す水平線
2. 最大収益日と最小収益日を強調する注釈
3. 読みやすさを向上させるためのカスタマイズされた目盛りパラメータ
4. より詳細なタイトルと凡例

ノートブックの新しいセルに以下のコードを追加して実行します。

```python
# Import the necessary module for formatting
import matplotlib.ticker as ticker

# Create a figure and axes
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue',
        linewidth=2, markersize=6, label='Daily Revenue')

# Calculate statistics
avg_revenue = np.mean(daily_revenue)
max_revenue = np.max(daily_revenue)
min_revenue = np.min(daily_revenue)
max_day = days[np.argmax(daily_revenue)]
min_day = days[np.argmin(daily_revenue)]

# Add a horizontal line for average revenue
ax.axhline(y=avg_revenue, color='r', linestyle='--', alpha=0.7,
           label=f'Average Revenue: ${avg_revenue:.2f}')

# Format y-axis with dollar signs
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)

# Customize tick parameters
ax.tick_params(axis='both', which='major', labelsize=10)
ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
ax.xaxis.set_major_locator(ticker.MultipleLocator(base=5))

# Add annotations for max and min revenue
ax.annotate(f'Max: ${max_revenue:.2f}', xy=(max_day, max_revenue),
            xytext=(max_day+1, max_revenue+200),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

ax.annotate(f'Min: ${min_revenue:.2f}', xy=(min_day, min_revenue),
            xytext=(min_day+1, min_revenue-200),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

# Add labels and title
ax.set_xlabel('Day of Month', fontsize=12)
ax.set_ylabel('Revenue ($)', fontsize=12)
ax.set_title('Daily Revenue Analysis - 30 Day Period', fontsize=14, fontweight='bold')

# Set x-axis limits to show a bit of padding
ax.set_xlim(0, 31)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add legend
ax.legend(loc='upper right', fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()

print("Enhanced financial plot created successfully!")
```

このコードを実行すると、以下の要素が追加された、はるかに情報量の多いプロットが表示されるはずです。

1. Y 軸にドル記号のフォーマット
2. 平均収益を示す水平の赤い破線
3. 最大収益日と最小収益日を指す注釈
4. 間隔が適切な、よりきれいな目盛り
5. 各要素が何を表すかを示す凡例

新しい要素のいくつかを説明しましょう。

- `ax.axhline()` - 指定された Y 値（この場合は平均収益）に水平線を追加します。
- `ax.yaxis.set_major_locator()` - Y 軸に表示される目盛りの数を制御します。
- `ax.xaxis.set_major_locator()` - X 軸を 5 日間隔で目盛りを表示するように設定します。
- `ax.annotate()` - 特定のデータポイントを指す矢印付きのテキスト注釈を追加します。
- `ax.legend()` - プロット上の異なる要素を説明する凡例を追加します。

これらの強化により、重要な統計情報が強調され、データが解釈しやすくなるため、プロットは金融分析にはるかに役立つものになります。
