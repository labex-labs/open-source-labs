# 예제의 미니배치를 반복하고 분류기를 업데이트합니다

```python
# 분류기에 1000 개의 문서로 구성된 미니배치를 제공합니다. 즉, 한 번에 메모리에 최대 1000 개의 문서가 있습니다.
# 문서 배치가 작을수록 부분적 적합 (partial fit) 메서드의 상대적 오버헤드가 커집니다.
minibatch_size = 1000

# Reuters SGML 파일을 파싱하고 문서를 스트림으로 반복하는 data_stream 을 생성합니다.
minibatch_iterators = iter_minibatches(data_stream, minibatch_size)
total_vect_time = 0.0

# 주요 루프: 예제의 미니배치를 반복합니다.
for i, (X_train_text, y_train) in enumerate(minibatch_iterators):
    tick = time.time()
    X_train = vectorizer.transform(X_train_text)
    total_vect_time += time.time() - tick

    for cls_name, cls in partial_fit_classifiers.items():
        tick = time.time()
        # 현재 미니배치의 예제로 추정자를 업데이트합니다.
        cls.partial_fit(X_train, y_train, classes=all_classes)

        # 테스트 정확도 통계를 누적합니다.
        cls_stats[cls_name]["total_fit_time"] += time.time() - tick
        cls_stats[cls_name]["n_train"] += X_train.shape[0]
        cls_stats[cls_name]["n_train_pos"] += sum(y_train)
        tick = time.time()
        cls_stats[cls_name]["accuracy"] = cls.score(X_test, y_test)
        cls_stats[cls_name]["prediction_time"] = time.time() - tick
        acc_history = (cls_stats[cls_name]["accuracy"], cls_stats[cls_name]["n_train"])
        cls_stats[cls_name]["accuracy_history"].append(acc_history)
        run_history = (
            cls_stats[cls_name]["accuracy"],
            total_vect_time + cls_stats[cls_name]["total_fit_time"],
        )
        cls_stats[cls_name]["runtime_history"].append(run_history)

        if i % 3 == 0:
            print(progress(cls_name, cls_stats[cls_name]))
    if i % 3 == 0:
        print("\n")
```
