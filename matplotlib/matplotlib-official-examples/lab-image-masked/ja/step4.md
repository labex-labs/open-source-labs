# 散布図の作成

折れ線グラフに加えて、Matplotlib は散布図の作成も可能です。散布図は、2 つの変数間の関係を視覚化するのに役立ちます。

```python
# Create the data
x = np.random.rand(50)
y = np.random.rand(50)

# Create the scatter plot
plt.scatter(x, y)

# Add title and axis labels
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
```
