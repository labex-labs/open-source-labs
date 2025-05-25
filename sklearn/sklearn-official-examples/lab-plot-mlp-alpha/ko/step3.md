# 분류기 생성

각 알파 값에 대해 MLP 분류기를 생성합니다. 데이터를 표준화하는 StandardScaler 와 다양한 알파 값을 가진 MLPClassifier 를 포함하는 파이프라인을 생성합니다. 최적화기로 quasi-Newton 계열의 'lbfgs'를 사용합니다. 과적합을 방지하기 위해 max_iter 를 2000 으로, early_stopping 을 True 로 설정합니다. 각각 10 개의 뉴런을 가진 두 개의 은닉층을 사용합니다.

```python
classifiers = []
names = []
for alpha in alphas:
    classifiers.append(
        make_pipeline(
            StandardScaler(),
            MLPClassifier(
                solver="lbfgs",
                alpha=alpha,
                random_state=1,
                max_iter=2000,
                early_stopping=True,
                hidden_layer_sizes=[10, 10],
            ),
        )
    )
    names.append(f"alpha {alpha:.2f}")
```
