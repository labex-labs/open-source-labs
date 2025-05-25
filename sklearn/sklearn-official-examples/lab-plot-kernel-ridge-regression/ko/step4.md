# 결과 확인

그리드 검색을 통해 RBF 커널의 복잡도/규제 및 밴드폭을 최적화했을 때 학습된 KRR 및 SVR 모델을 시각화합니다.

```python
import matplotlib.pyplot as plt

sv_ind = svr.best_estimator_.support_
plt.scatter(
    X[sv_ind],
    y[sv_ind],
    c="r",
    s=50,
    label="SVR support vectors",
    zorder=2,
    edgecolors=(0, 0, 0),
)
plt.scatter(X[:100], y[:100], c="k", label="data", zorder=1, edgecolors=(0, 0, 0))
plt.plot(
    X_plot,
    y_svr,
    c="r",
    label="SVR (fit: %.3fs, predict: %.3fs)" % (svr_fit, svr_predict),
)
plt.plot(
    X_plot, y_kr, c="g", label="KRR (fit: %.3fs, predict: %.3fs)" % (kr_fit, kr_predict)
)
plt.xlabel("데이터")
plt.ylabel("타겟")
plt.title("SVR 대 커널 릿지")
_ = plt.legend()
```
