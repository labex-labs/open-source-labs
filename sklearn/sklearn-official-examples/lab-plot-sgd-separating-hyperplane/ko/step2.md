# SGD 를 사용한 SVM 모델 학습

다음으로, SGD 를 사용하여 SVM 모델을 학습해야 합니다. Scikit-learn 의 `SGDClassifier` 클래스를 사용하여 모델을 학습합니다. SVM 알고리즘을 사용하기 위해 `loss` 매개변수를 "hinge"로 설정하고 정규화 강도를 제어하기 위해 `alpha` 매개변수를 0.01 로 설정합니다. 또한 반복 횟수를 제한하기 위해 `max_iter` 매개변수를 200 으로 설정합니다.

```python
# 모델 학습
clf = SGDClassifier(loss="hinge", alpha=0.01, max_iter=200)
clf.fit(X, Y)
```
