# 분류기 학습

이제 scikit-learn 의 SGDClassifier 클래스를 사용하여 SGD 분류기를 생성하고 학습할 수 있습니다. 선형 분류기에 일반적으로 사용되는 'hinge' 손실 함수를 사용합니다.

```python
clf = SGDClassifier(loss='hinge', random_state=42)
clf.fit(X_train, y_train)
```
