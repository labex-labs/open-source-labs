# データセットを可視化する

ここでは、matplotlib を使ってデータセットを可視化します。X の値に対して y の値をプロットします。

```python
plt.plot(X, y, "b.")
plt.title("Dataset with Strong Outliers")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
