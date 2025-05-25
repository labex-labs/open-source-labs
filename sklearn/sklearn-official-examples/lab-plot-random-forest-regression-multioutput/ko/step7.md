# 결과 플롯

두 회귀 모델의 성능을 비교하기 위해 결과를 플롯합니다. `matplotlib`를 사용하여 실제 테스트 데이터, 랜덤 포레스트 회귀 모델의 예측값, 그리고 다중 출력 회귀 모델의 예측값을 산점도로 표시합니다.

```python
plt.figure()
s = 50
a = 0.4
plt.scatter(y_test[:, 0], y_test[:, 1], edgecolor="k", c="navy", s=s, marker="s", alpha=a, label="Data")
plt.scatter(y_rf[:, 0], y_rf[:, 1], edgecolor="k", c="c", s=s, marker="^", alpha=a, label="RF score=%.2f" % regr_rf.score(X_test, y_test))
plt.scatter(y_multirf[:, 0], y_multirf[:, 1], edgecolor="k", c="cornflowerblue", s=s, alpha=a, label="Multi RF score=%.2f" % regr_multirf.score(X_test, y_test))
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.xlabel("target 1")
plt.ylabel("target 2")
plt.title("랜덤 포레스트와 다중 출력 메타 추정기 비교")
plt.legend()
plt.show()
```
