# 벡터라이저 설정 및 테스트 세트 분리

```python
# 벡터라이저를 생성하고, 특징 수를 적절한 최대값으로 제한합니다.
vectorizer = HashingVectorizer(decode_error="ignore", n_features=2**18, alternate_sign=False)

# 파싱된 Reuters SGML 파일을 반복하는 반복자.
data_stream = stream_reuters_documents()

# "acq" 클래스와 다른 모든 클래스 간의 이진 분류를 학습합니다.
# "acq"는 Reuters 파일에서 거의 균등하게 분포되어 있기 때문에 선택되었습니다.
# 다른 데이터셋의 경우, 양성 인스턴스의 현실적인 비율로 테스트 세트를 만드는 데 주의해야 합니다.
all_classes = np.array([0, 1])
positive_class = "acq"

# `partial_fit` 메서드를 지원하는 몇 가지 분류기가 있습니다.
partial_fit_classifiers = {
    "SGD": SGDClassifier(max_iter=5),
    "Perceptron": Perceptron(),
    "NB Multinomial": MultinomialNB(alpha=0.01),
    "Passive-Aggressive": PassiveAggressiveClassifier(),
}

# 테스트 데이터 통계
test_stats = {"n_test": 0, "n_test_pos": 0}

# 먼저 정확도를 추정하기 위해 일부 예제를 분리합니다.
n_test_documents = 1000
X_test_text, y_test = get_minibatch(data_stream, 1000)
X_test = vectorizer.transform(X_test_text)
test_stats["n_test"] += len(y_test)
test_stats["n_test_pos"] += sum(y_test)
print("테스트 세트는 %d개의 문서 (%d개의 양성)" % (len(y_test), sum(y_test)))
```
