# 単純な折れ線グラフの作成

X軸の値が0から5の範囲で、対応するY軸の値を持つ単純な折れ線グラフを作成します。`pyplot` モジュールによって提供される `plot` 関数を使用して折れ線グラフを作成します。

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a line plot
plt.plot(x, y)

# Adding title and labels to the plot
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```
