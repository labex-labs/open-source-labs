# 모델 학습 및 평가

이제 학습 데이터셋으로 서포트 벡터 머신 (SVM) 분류기를 학습하고 테스트 데이터셋으로 성능을 평가해 보겠습니다.

```python
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
score = clf.score(X_test, y_test)
print("Accuracy: ", score)
```
