# 랜덤 포레스트 분류기 학습

먼저 위스콘신 유방암 데이터셋을 불러와서 학습용과 테스트용 데이터셋으로 분할합니다. 그런 다음 학습 데이터셋으로 랜덤 포레스트 분류기를 학습하고 테스트 데이터셋에서 정확도를 평가합니다.

```python
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
print("Accuracy on test data: {:.2f}".format(clf.score(X_test, y_test)))
```
