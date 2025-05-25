# 가중치가 부여된 모델 학습

4 단계와 동일한 알고리즘을 사용하여 가중치가 부여된 모델을 학습합니다. 이번에는 `fit` 메서드에 `sample_weight` 인수를 전달합니다. 그런 다음 가중치가 부여된 모델의 결정 함수를 시각화합니다.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y, sample_weight=sample_weight)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
samples_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["dashed"])
```
