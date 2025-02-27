# データの可視化

真の関数と生成したサンプルをプロットします。

```python
plt.figure(figsize=(6, 4))
plt.plot(np.linspace(0, 1, 100), true_fun(np.linspace(0, 1, 100)), label="True function")
plt.scatter(X, y, edgecolor="b", s=20, label="Samples")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="best")
plt.show()
```
