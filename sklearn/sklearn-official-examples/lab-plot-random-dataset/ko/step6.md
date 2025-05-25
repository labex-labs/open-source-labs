# 다중 클래스, 두 개의 정보 특징, 하나의 클러스터

여러 클래스, 두 개의 정보 특징, 그리고 하나의 클러스터를 가진 데이터셋을 생성하고 플롯합니다.

```python
plt.subplot(324)
plt.title("다중 클래스, 두 개의 정보 특징, 하나의 클러스터", fontsize="small")
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=2, n_clusters_per_class=1, n_classes=3)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```
