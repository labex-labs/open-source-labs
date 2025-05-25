# 세 개의 블롭

세 개의 블롭으로 구성된 데이터셋을 생성하고 플롯합니다.

```python
plt.subplot(325)
plt.title("세 개의 블롭", fontsize="small")
X1, Y1 = make_blobs(n_features=2, centers=3)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```
