# 結果を可視化する

最後に、等張回帰モデルの結果を可視化しましょう。元のデータポイントを散布図として、予測値を線としてプロットすることができます。

```python
import matplotlib.pyplot as plt

# Plot the original data and predicted values
plt.scatter(X, y, c='b', label='Original Data')
plt.plot(X_new, y_pred, c='r', label='Isotonic Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
