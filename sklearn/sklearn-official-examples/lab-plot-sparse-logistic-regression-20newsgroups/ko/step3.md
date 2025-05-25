# 모델 정의 및 학습

다항 분류 (Multinomial) 및 One-vs-Rest L1 로지스틱 회귀 모델을 정의하고, 다른 에포크 수로 학습합니다.

```python
models = {
    "ovr": {"name": "One versus Rest", "iters": [1, 2, 3]},
    "multinomial": {"name": "Multinomial", "iters": [1, 2, 5]},
}

for model in models:
    # 플롯을 위해 초기 확률 수준 값 추가
    accuracies = [1 / n_classes]
    times = [0]
    densities = [1]

    model_params = models[model]

    # 빠른 실행 시간을 위해 에포크 수를 적게 설정
    for this_max_iter in model_params["iters"]:
        print(
            "[model=%s, solver=%s] 에포크 수: %s"
            % (model_params["name"], solver, this_max_iter)
        )
        lr = LogisticRegression(
            solver=solver,
            multi_class=model,
            penalty="l1",
            max_iter=this_max_iter,
            random_state=42,
        )
        t1 = timeit.default_timer()
        lr.fit(X_train, y_train)
        train_time = timeit.default_timer() - t1

        y_pred = lr.predict(X_test)
        accuracy = np.sum(y_pred == y_test) / y_test.shape[0]
        density = np.mean(lr.coef_ != 0, axis=1) * 100
        accuracies.append(accuracy)
        densities.append(density)
        times.append(train_time)
    models[model]["times"] = times
    models[model]["densities"] = densities
    models[model]["accuracies"] = accuracies
    print("모델 %s의 테스트 정확도: %.4f" % (model, accuracies[-1]))
    print(
        "모델 %s의 클래스별 비 -0 계수 비율:\n %s"
        % (model, densities[-1])
    )
    print(
        "모델 %s의 실행 시간 (%i 에포크): %.2f"
        % (model, model_params["iters"][-1], times[-1])
    )
```
