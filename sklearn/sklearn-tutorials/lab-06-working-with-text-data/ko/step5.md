# 모델 평가

모델의 성능을 평가하기 위해 별도의 테스트 데이터셋을 사용합니다. 학습 데이터셋과 동일한 방법으로 테스트 데이터셋을 로드합니다.

```python
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
```

이제 테스트 데이터셋을 전처리하고 특징 벡터를 추출합니다.

```python
X_test_counts = count_vect.transform(twenty_test.data)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)
```

마지막으로, 학습된 모델을 사용하여 테스트 데이터셋에 대한 예측을 수행하고 정확도를 계산합니다.

```python
predicted = clf.predict(X_test_tfidf)
accuracy = np.mean(predicted == twenty_test.target)
```
