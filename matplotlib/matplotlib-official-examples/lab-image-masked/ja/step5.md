# 棒グラフの作成

もう一つ一般的なグラフの種類は棒グラフです。棒グラフは、異なるカテゴリの値を比較するのに役立ちます。

```python
# Create the data
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 1, 9, 4]

# Create the bar chart
plt.bar(x, y)

# Add title and axis labels
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()
```
