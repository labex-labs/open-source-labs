# PCA 수행

다음으로, 데이터에서 가장 큰 분산을 차지하는 속성 조합을 식별하기 위해 주성분 분석 (PCA) 을 데이터셋에 적용합니다. 첫 번째와 두 번째 주성분에 대한 서로 다른 샘플을 플롯합니다.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

# 각 구성요소에 대한 설명된 분산의 백분율
print("설명된 분산 비율 (첫 두 구성요소): %s" % str(pca.explained_variance_ratio_))

plt.figure()
colors = ["navy", "turquoise", "darkorange"]
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name)

plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("아이리스 데이터셋의 PCA")
plt.show()
```
