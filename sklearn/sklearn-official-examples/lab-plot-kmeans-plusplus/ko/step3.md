# 샘플 데이터와 함께 초기 시드 플롯

matplotlib 라이브러리를 사용하여 샘플 데이터와 함께 초기 시드를 플롯합니다. 초기 시드는 파란색 점으로 표시되고, 샘플 데이터는 색상이 있는 점으로 표시됩니다.

```python
# 샘플 데이터와 함께 초기 시드 플롯
plt.figure(1)
colors = ["#4EACC5", "#FF9C34", "#4E9A06", "m"]

for k, col in enumerate(colors):
    cluster_data = y_true == k
    plt.scatter(X[cluster_data, 0], X[cluster_data, 1], c=col, marker=".", s=10)

plt.scatter(centers_init[:, 0], centers_init[:, 1], c="b", s=50)
plt.title("K-Means++ 초기화")
plt.xticks([])
plt.yticks([])
plt.show()
```
