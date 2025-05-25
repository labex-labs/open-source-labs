# 두 개의 정보 특징, 클래스당 두 개의 클러스터

두 개의 정보 특징과 클래스당 두 개의 클러스터를 가진 데이터셋을 생성하고 플롯합니다.

```python
plt.subplot(323)
plt.title("두 개의 정보 특징, 클래스당 두 개의 클러스터", fontsize="small")
X2, Y2 = make_classification(n_features=2, n_redundant=0, n_informative=2)
plt.scatter(X2[:, 0], X2[:, 1], marker="o", c=Y2, s=25, edgecolor="k")
```
