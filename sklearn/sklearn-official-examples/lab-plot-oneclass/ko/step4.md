# 결과 시각화

마지막으로, 일원 SVM 모델의 결과를 시각화합니다. 결정 경계, 학습 데이터, 일반적인 새로운 관측치 및 비정상적인 새로운 관측치를 플롯합니다.

```python
# 결과 시각화
xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title("새로운 데이터 검출")
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
        "학습 관측치",
        "새로운 일반 관측치",
        "새로운 비정상 관측치",
    ],
    loc="upper left",
    prop=matplotlib.font_manager.FontProperties(size=11),
)
plt.xlabel(
    "오류 학습: %d/200 ; 오류 새로운 일반: %d/40 ; 오류 새로운 비정상: %d/40"
    % (n_error_train, n_error_test, n_error_outliers)
)
plt.show()
```
