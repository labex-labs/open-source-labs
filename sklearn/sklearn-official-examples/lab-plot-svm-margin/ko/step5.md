# 등고선 플롯

결정 함수의 등고선을 플롯합니다. 먼저 `xx`와 `yy` 배열을 사용하여 메쉬 그리드를 생성합니다. 그런 다음 메쉬 그리드를 2 차원 배열로 변환하고 `SVC` 클래스의 `decision_function` 메서드를 적용하여 예측 값을 얻습니다. 그런 다음 `contourf` 메서드를 사용하여 등고선을 플롯합니다.

```python
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

plt.contourf(XX, YY, Z, cmap=plt.get_cmap("RdBu"), alpha=0.5, linestyles=["-"])

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.xticks(())
plt.yticks(())
```
