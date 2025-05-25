# 모델 학습

이제 특징 벡터를 얻었으므로 텍스트 데이터를 분류하는 모델을 학습시킬 수 있습니다. 이 예제에서는 텍스트 분류에 널리 사용되는 다항분포 나이브 베이즈 (Multinomial Naive Bayes) 알고리즘을 사용합니다.

```python
from sklearn.naive_bayes import MultinomialNB

# 모델 학습
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
```

이제 모델이 학습되어 예측 준비가 완료되었습니다.
