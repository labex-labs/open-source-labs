# 円グラフの作成

異なるデータポイントを表す5つのセクションを持つ円グラフを作成します。`pyplot` モジュールによって提供される `pie` 関数を使用して円グラフを作成します。

```python
# Creating data for the pie chart
data = [10, 20, 30, 25, 15]

# Creating labels for the pie chart
labels = ['Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5']

# Creating a pie chart
plt.pie(data, labels=labels)

# Adding title to the plot
plt.title('Pie Chart')

# Displaying the plot
plt.show()
```
