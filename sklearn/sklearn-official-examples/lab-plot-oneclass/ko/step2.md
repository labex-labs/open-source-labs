# 일원 SVM 모델 학습

다음으로 생성된 데이터에 대한 일원 SVM 모델을 학습합니다.

```python
# 모델 학습
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)

# 학습 데이터, 일반적인 새로운 관측치 및 비정상적인 새로운 관측치에 대한 레이블 예측
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
```
