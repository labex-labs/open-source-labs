# 특징 추출

텍스트 데이터를 특징 벡터로 표현하기 위해 단어 빈도수 (bag of words) 표현을 사용할 수 있습니다. 이 표현은 학습 데이터셋의 각 단어에 고정된 정수 ID 를 할당하고 각 문서에서 각 단어의 출현 횟수를 계산합니다. scikit-learn 의 `CountVectorizer`를 사용하여 이러한 특징 벡터를 추출할 수 있습니다.

```python
from sklearn.feature_extraction.text import CountVectorizer

# 특징 벡터 추출
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
```

이제 특징 벡터를 추출했으므로 이를 사용하여 모델을 학습시킬 수 있습니다.
