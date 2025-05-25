# 최대 마진 분류 초평면 플롯

최대 마진 분류 초평면을 플롯하기 위해 scikit-learn 의 `DecisionBoundaryDisplay.from_estimator()` 함수를 사용합니다. 이 함수는 SVM 분류기의 결정 함수와 지원 벡터를 플롯합니다. 또한 지원 벡터를 채워지지 않은 원으로 플롯하고 검은색 테두리를 추가합니다.

```python
from sklearn.inspection import DecisionBoundaryDisplay

# 결정 함수와 지원 벡터 플롯
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    plot_method="contour",
    colors="k",
    levels=[-1, 0, 1],
    alpha=0.5,
    linestyles=["--", "-", "--"],
    ax=ax,
)
ax.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=100,
    linewidth=1,
    facecolors="none",
    edgecolors="k",
)
plt.show()
```
