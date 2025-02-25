# グラフを作成する

これで、カスタム チェッカー付きのグラフを作成できます。サンプル データを使って棒グラフを作成し、y 軸の目盛りにカスタム チェッカー関数を使うように設定します。

```python
# Create a bar chart with sample data
fig, ax = plt.subplots()
money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]
ax.bar(['Bill', 'Fred', 'Mary', 'Sue'], money)

# Set the y-axis ticker to use the custom ticker function
ax.yaxis.set_major_formatter(ticker.FuncFormatter(millions))

# Display the plot
plt.show()
```
