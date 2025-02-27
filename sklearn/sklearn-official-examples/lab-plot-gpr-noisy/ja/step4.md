# データ可視化

このステップでは、ノイズ付きの学習データセットと期待信号を一緒に可視化します。

```python
plt.plot(X, y, label="Expected signal")
plt.scatter(
    x=X_train[:, 0],
    y=y_train,
    color="black",
    alpha=0.4,
    label="Observations",
)
plt.legend()
plt.xlabel("X")
_ = plt.ylabel("y")
```
