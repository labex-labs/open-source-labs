# MLP 모델 생성 및 학습

```python
# 5 개의 뉴런으로 이루어진 하나의 은닉층을 가진 MLP 분류기를 생성합니다.
clf = MLPClassifier(hidden_layer_sizes=(5,), random_state=1)

# 학습 데이터를 사용하여 모델을 학습합니다.
clf.fit(X, y)
```
