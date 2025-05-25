# 이차원 데이터에서 이상치 탐지

이차원 와인 데이터셋에서 이상치 탐지를 수행합니다. 이상치를 탐지하기 위해 Empirical Covariance, Robust Covariance, 그리고 One-Class SVM 의 세 가지 다른 분류기를 사용하고, 그 결과를 시각화합니다.

```python
# 여러 분류기를 사용하여 이상치 탐지 경계 학습
xx1, yy1 = np.meshgrid(np.linspace(0, 6, 500), np.linspace(1, 4.5, 500))
for i, (clf_name, clf) in enumerate(classifiers.items()):
    plt.figure(1)
    clf.fit(X1)
    Z1 = clf.decision_function(np.c_[xx1.ravel(), yy1.ravel()])
    Z1 = Z1.reshape(xx1.shape)
    plt.contour(
        xx1, yy1, Z1, levels=[0], linewidths=2, colors=colors[i]
    )

# 결과 플롯 (= 데이터 포인트 클라우드의 모양)
plt.figure(1)  # 두 개의 클러스터
plt.title("실제 데이터셋 (와인 인식) 에서 이상치 탐지")
plt.scatter(X1[:, 0], X1[:, 1], color="black")
plt.xlim((xx1.min(), xx1.max()))
plt.ylim((yy1.min(), yy1.max()))
plt.ylabel("ash")
plt.xlabel("malic_acid")
plt.show()
```
