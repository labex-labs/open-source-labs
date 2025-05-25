# 가우시안을 세 개의 사분위수로 나눈 데이터

가우시안 분포를 세 개의 사분위수로 나눈 데이터셋을 생성하고 플롯합니다.

```python
plt.subplot(326)
plt.title("가우시안을 세 개의 사분위수로 나눈 데이터", fontsize="small")
X1, Y1 = make_gaussian_quantiles(n_features=2, n_classes=3)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```
