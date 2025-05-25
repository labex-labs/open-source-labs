# 사후 확률 플롯

고정 및 최적화된 하이퍼파라미터를 사용하여 GPC 모델의 사후 확률을 플롯합니다. 학습 데이터, 테스트 데이터 및 클래스 1 의 예측 확률을 플롯합니다. 또한 플롯에 레이블을 지정합니다.

```python
# 사후 확률 플롯
plt.figure()
plt.scatter(X[:train_size, 0], y[:train_size], c="k", label="Train data", edgecolors=(0, 0, 0))
plt.scatter(X[train_size:, 0], y[train_size:], c="g", label="Test data", edgecolors=(0, 0, 0))
X_ = np.linspace(0, 5, 100)
plt.plot(X_, gp_fix.predict_proba(X_[:, np.newaxis])[:, 1], "r", label="Initial kernel: %s" % gp_fix.kernel_)
plt.plot(X_, gp_opt.predict_proba(X_[:, np.newaxis])[:, 1], "b", label="Optimized kernel: %s" % gp_opt.kernel_)
plt.xlabel("특징")
plt.ylabel("클래스 1 확률")
plt.xlim(0, 5)
plt.ylim(-0.25, 1.5)
plt.legend(loc="best")
```
