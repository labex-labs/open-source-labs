# 의사결정 트리 분류기 생성 및 학습

이제 학습 데이터를 사용하여 의사결정 트리 분류기를 생성하고 학습할 수 있습니다.

```python
# 의사결정 트리 분류기 생성
clf = tree.DecisionTreeClassifier()

# 분류기 학습
clf.fit(X_train, y_train)
```
