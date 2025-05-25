# AUC 계산

이 단계에서는 배경 지점에 대한 ROC 곡선 아래 면적 (AUC) 을 계산합니다. 테스트 데이터와 배경 지점을 사용하여 종 분포를 예측하고 AUC 를 계산합니다.

```python
# 배경 지점에 대한 AUC 계산
background_points = np.c_[
    np.random.randint(low=0, high=data.Ny, size=10000),
    np.random.randint(low=0, high=data.Nx, size=10000),
].T

pred_background = Z[background_points[0], background_points[1]]
pred_test = clf.decision_function((BV_bunch.cov_test - mean) / std)
scores = np.r_[pred_test, pred_background]
y = np.r_[np.ones(pred_test.shape), np.zeros(pred_background.shape)]
fpr, tpr, thresholds = metrics.roc_curve(y, scores)
roc_auc = metrics.auc(fpr, tpr)
plt.text(-35, -70, "AUC: %.3f" % roc_auc, ha="right")
print("\n ROC 곡선 아래 면적 : %f" % roc_auc)
```
