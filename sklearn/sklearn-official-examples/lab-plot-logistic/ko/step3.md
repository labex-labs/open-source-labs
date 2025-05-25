# 분류기 학습

데이터셋을 생성한 후, scikit-learn 의 `LogisticRegression`을 사용하여 분류기를 학습합니다.

```python
# 분류기 학습
clf = LogisticRegression(C=1e5)
clf.fit(X, y)
```
