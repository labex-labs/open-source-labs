# データセットを可視化する

ここでは、matplotlibを使ってデータセットを可視化します。Xの値に対してyの値をプロットします。

```python
plt.plot(X, y, "b.")
plt.title("Dataset with Strong Outliers")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
