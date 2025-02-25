# データの作成

次に、グラフに使用するデータを作成します。このチュートリアルでは、単純な折れ線グラフを作成します。

```python
# Create the data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y)
plt.show()
```
