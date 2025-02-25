# 散布図の作成

0から5の範囲のX軸の値と対応するY軸の値を持つ散布図を作成します。`pyplot` モジュールによって提供される `scatter` 関数を使用して散布図を作成します。

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a scatter plot
plt.scatter(x, y)

# Adding title and labels to the plot
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```
