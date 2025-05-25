# 점수 및 확률

- SVM 은 직접 확률 추정값을 제공하지 않지만, `probability` 매개변수를 `True`로 설정하여 확률 추정을 활성화할 수 있습니다.

```python
clf = svm.SVC(probability=True)
clf.fit(X, y)
```

- 그런 다음 각 클래스의 확률을 얻으려면 `predict_proba` 메서드를 사용할 수 있습니다.

```python
clf.predict_proba([[2., 2.]])
```

- 확률 추정은 비용이 많이 들고 교차 검증이 필요하므로 신중하게 사용하십시오.
