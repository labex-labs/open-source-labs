# データを可視化する

生成したデータを散布図を使って可視化しましょう。

```python
# Plot the data points
plt.scatter(X[:, 0], X[:, 1])
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```
