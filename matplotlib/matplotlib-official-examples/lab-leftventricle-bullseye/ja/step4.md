# 棒グラフの作成

0から5の範囲のX軸の値と対応するY軸の値を持つ棒グラフを作成します。`pyplot` モジュールによって提供される `bar` 関数を使用して棒グラフを作成します。

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a bar plot
plt.bar(x, y)

# Adding title and labels to the plot
plt.title('Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```
