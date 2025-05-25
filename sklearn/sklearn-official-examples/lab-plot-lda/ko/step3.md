# 분류기 학습 및 테스트

생성된 데이터에서 각 분류기의 성능을 확인하기 위해 학습 및 테스트를 수행합니다. 평균 정확도 점수를 얻기 위해 이 과정을 여러 번 반복합니다.

```python
n_train = 20  # 학습용 샘플 수
n_test = 200  # 테스트용 샘플 수
n_averages = 50  # 분류를 반복할 횟수
n_features_max = 75  # 특징의 최대 개수
step = 4  # 계산 단계 크기

acc_clf1, acc_clf2, acc_clf3 = [], [], []
n_features_range = range(1, n_features_max + 1, step)

for n_features in n_features_range:
    score_clf1, score_clf2, score_clf3 = 0, 0, 0
    for _ in range(n_averages):
        X, y = generate_data(n_train, n_features)

        clf1.fit(X, y)
        clf2.fit(X, y)
        clf3.fit(X, y)

        X, y = generate_data(n_test, n_features)
        score_clf1 += clf1.score(X, y)
        score_clf2 += clf2.score(X, y)
        score_clf3 += clf3.score(X, y)

    acc_clf1.append(score_clf1 / n_averages)
    acc_clf2.append(score_clf2 / n_averages)
    acc_clf3.append(score_clf3 / n_averages)
```
