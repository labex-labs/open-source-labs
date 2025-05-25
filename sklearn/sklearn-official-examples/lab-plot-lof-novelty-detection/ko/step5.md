# 결과 시각화

학습된 경계와 함께 훈련 데이터, 테스트 데이터, 이상치 데이터를 플롯하여 결과를 시각화합니다. 또한 테스트 데이터와 이상치 데이터의 오류 수를 표시합니다.

```python
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title("LOF 를 이용한 신규 데이터 검출")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors="darkred")
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors="palevioletred")

s = 40
b1 = plt.scatter(X_train[:, 0], X_train[:, 1], c="white", s=s, edgecolors="k")
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], c="blueviolet", s=s, edgecolors="k")
c = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], c="gold", s=s, edgecolors="k")
plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend(
    [a.collections[0], b1, b2, c],
    [
        "학습된 경계",
        "훈련 관측치",
        "새로운 일반 관측치",
        "새로운 비정상 관측치",
    ],
    loc="upper left",
    prop=matplotlib.font_manager.FontProperties(size=11),
)
plt.xlabel(
    "오류 (새로운 일반: %d/40 ; 새로운 비정상: %d/40)"
    % (n_error_test, n_error_outliers)
)
plt.show()
```
