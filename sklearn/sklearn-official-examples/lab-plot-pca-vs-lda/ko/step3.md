# LDA 수행

이제, 클래스 간의 가장 큰 분산을 설명하는 속성을 식별하기 위해 선형 판별 분석 (LDA) 을 데이터셋에 적용합니다. PCA 와 달리 LDA 는 알려진 클래스 레이블을 사용하는 지도 학습 방법입니다.

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(X, y).transform(X)

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], alpha=0.8, color=color, label=target_name)

plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("아이리스 데이터셋의 LDA")
plt.show()
```
