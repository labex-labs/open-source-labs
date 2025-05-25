# L1 패널티 적용

이제 SGDClassifier 를 사용하여 데이터에 L1 패널티를 적용합니다.

```python
# L1 패널티를 가진 분류기 생성
clf = SGDClassifier(loss='hinge', penalty='l1', alpha=0.05, max_iter=1000, tol=1e-3)

# 모델 학습
clf.fit(X, y)

# 결정 경계 시각화
plt.scatter(X[:, 0], X[:, 1], c=y)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 201), np.linspace(ylim[0], ylim[1], 201))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
ax.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
ax.set_xlim(xlim)
ax.set_ylim(ylim)
plt.title('L1 Penalty')
plt.show()
```
