# MLE 및 MCD 마할라노비스 거리 비교

이상치를 구분하는 MCD 기반 마할라노비스 거리의 능력을 강조합니다. 마할라노비스 거리의 세제곱근을 취하여 대략 정규 분포를 얻습니다. 그런 다음, 상자 그림으로 내부 및 외부 샘플의 값을 플롯합니다. 강력한 MCD 기반 마할라노비스 거리의 경우 이상치 샘플의 분포가 내부 샘플의 분포에서 더 분리되어 있습니다.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
plt.subplots_adjust(wspace=0.6)

# 샘플에 대한 MLE 마할라노비스 거리의 세제곱근 계산
emp_mahal = emp_cov.mahalanobis(X - np.mean(X, 0)) ** (0.33)
# 상자 그림 플롯
ax1.boxplot([emp_mahal[:-n_outliers], emp_mahal[-n_outliers:]], widths=0.25)
# 개별 샘플 플롯
ax1.plot(
    np.full(n_samples - n_outliers, 1.26),
    emp_mahal[:-n_outliers],
    "+k",
    markeredgewidth=1,
)
ax1.plot(np.full(n_outliers, 2.26), emp_mahal[-n_outliers:], "+k", markeredgewidth=1)
ax1.axes.set_xticklabels(("inliers", "outliers"), size=15)
ax1.set_ylabel(r"$\sqrt[3]{\rm{(Mahal. dist.)}}$", size=16)
ax1.set_title("비강력 추정 사용\n(최대 가능도)")

# 샘플에 대한 MCD 마할라노비스 거리의 세제곱근 계산
robust_mahal = robust_cov.mahalanobis(X - robust_cov.location_) ** (0.33)
# 상자 그림 플롯
ax2.boxplot([robust_mahal[:-n_outliers], robust_mahal[-n_outliers:]], widths=0.25)
# 개별 샘플 플롯
ax2.plot(
    np.full(n_samples - n_outliers, 1.26),
    robust_mahal[:-n_outliers],
    "+k",
    markeredgewidth=1,
)
ax2.plot(np.full(n_outliers, 2.26), robust_mahal[-n_outliers:], "+k", markeredgewidth=1)
ax2.axes.set_xticklabels(("inliers", "outliers"), size=15)
ax2.set_ylabel(r"$\sqrt[3]{\rm{(Mahal. dist.)}}$", size=16)
ax2.set_title("강력 추정 사용\n(최소 공분산 행렬)")

plt.show()
```
