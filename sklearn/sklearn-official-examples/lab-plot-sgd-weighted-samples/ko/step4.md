# 가중치 없는 모델 학습

scikit-learn 라이브러리의 SGDClassifier 알고리즘을 사용하여 가중치 없는 모델을 학습합니다. 그런 다음 가중치 없는 모델의 결정 함수를 시각화합니다.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
no_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["solid"])
```
