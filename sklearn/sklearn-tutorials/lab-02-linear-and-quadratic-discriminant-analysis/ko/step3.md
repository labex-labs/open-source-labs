# 분류기를 학습하고 시각화하기

이제 합성 데이터에 LDA 와 QDA 분류기를 학습하고 결정 경계를 시각화합니다.

```python
# LDA 분류기를 학습합니다.
lda = LinearDiscriminantAnalysis()
lda.fit(X, y)

# QDA 분류기를 학습합니다.
qda = QuadraticDiscriminantAnalysis()
qda.fit(X, y)

# 결정 경계를 그립니다.
def plot_decision_boundary(classifier, title):
    h = 0.02  # 메쉬의 간격
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.Paired)
    plt.xlabel('특징 1')
    plt.ylabel('특징 2')
    plt.title(title)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plot_decision_boundary(lda, '선형 판별 분석')

plt.subplot(1, 2, 2)
plot_decision_boundary(qda, '2 차 판별 분석')

plt.tight_layout()
plt.show()
```
