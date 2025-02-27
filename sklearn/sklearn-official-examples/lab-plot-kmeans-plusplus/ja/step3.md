# 初期シードとサンプルデータを並べてプロットする

matplotlibライブラリを使って、初期シードとサンプルデータを並べてプロットします。初期シードは青い点として表示され、サンプルデータは色付きの点として表示されます。

```python
# Plot init seeds along side sample data
plt.figure(1)
colors = ["#4EACC5", "#FF9C34", "#4E9A06", "m"]

for k, col in enumerate(colors):
    cluster_data = y_true == k
    plt.scatter(X[cluster_data, 0], X[cluster_data, 1], c=col, marker=".", s=10)

plt.scatter(centers_init[:, 0], centers_init[:, 1], c="b", s=50)
plt.title("K-Means++ Initialization")
plt.xticks([])
plt.yticks([])
plt.show()
```
