# MLPClassifier 학습

40 개의 뉴런을 포함하는 단일 은닉층을 가진 MLPClassifier 를 생성합니다. 자원 제약으로 인해 MLP 를 8 번의 반복만 학습시킵니다. 또한, 모델이 제한된 반복 횟수 내에 수렴하지 않아 발생하는 `ConvergenceWarning`을 처리합니다.

```python
mlp = MLPClassifier(
    hidden_layer_sizes=(40,),
    max_iter=8,
    alpha=1e-4,
    solver="sgd",
    verbose=10,
    random_state=1,
    learning_rate_init=0.2,
)

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=ConvergenceWarning, module="sklearn")
    mlp.fit(X_train, y_train)
```
