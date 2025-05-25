# 모델 평가

모델의 성능을 희소성 (sparsity) 과 정확도 (accuracy) 점수를 계산하여 평가합니다.

```python
sparsity = np.mean(clf.coef_ == 0) * 100
score = clf.score(X_test, y_test)

print("L1 페널티를 사용한 희소성: %.2f%%" % sparsity)
print("L1 페널티를 사용한 테스트 점수: %.4f" % score)
```
