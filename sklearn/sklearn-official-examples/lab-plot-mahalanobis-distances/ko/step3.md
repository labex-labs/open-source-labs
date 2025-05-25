# 마할라노비스 거리의 등고선 플롯

두 방법 모두로 계산된 마할라노비스 거리의 등고선을 플롯합니다. 강력한 MCD 기반 마할라노비스 거리는 내부 점인 검은색 점에 훨씬 더 잘 맞는 반면, MLE 기반 거리는 이상치인 빨간색 점에 더 큰 영향을 받습니다.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))
# 데이터 집합 플롯
inlier_plot = ax.scatter(X[:, 0], X[:, 1], color="black", label="inliers")
outlier_plot = ax.scatter(
    X[:, 0][-n_outliers:], X[:, 1][-n_outliers:], color="red", label="outliers"
)
ax.set_xlim(ax.get_xlim()[0], 10.0)
ax.set_title("오염된 데이터 집합의 마할라노비스 거리")

# 특징 1 과 특징 2 값의 메쉬 그리드 생성
xx, yy = np.meshgrid(
    np.linspace(plt.xlim()[0], plt.xlim()[1], 100),
    np.linspace(plt.ylim()[0], plt.ylim()[1], 100),
)
zz = np.c_[xx.ravel(), yy.ravel()]
# 메쉬 그리드의 MLE 기반 마할라노비스 거리 계산
mahal_emp_cov = emp_cov.mahalanobis(zz)
mahal_emp_cov = mahal_emp_cov.reshape(xx.shape)
emp_cov_contour = plt.contour(
    xx, yy, np.sqrt(mahal_emp_cov), cmap=plt.cm.PuBu_r, linestyles="dashed"
)
# MCD 기반 마할라노비스 거리 계산
mahal_robust_cov = robust_cov.mahalanobis(zz)
mahal_robust_cov = mahal_robust_cov.reshape(xx.shape)
robust_contour = ax.contour(
    xx, yy, np.sqrt(mahal_robust_cov), cmap=plt.cm.YlOrBr_r, linestyles="dotted"
)

# 범례 추가
ax.legend(
    [
        emp_cov_contour.collections[1],
        robust_contour.collections[1],
        inlier_plot,
        outlier_plot,
    ],
    ["MLE 거리", "MCD 거리", "내부 점", "이상치"],
    loc="upper right",
    borderaxespad=0,
)

plt.show()
```
