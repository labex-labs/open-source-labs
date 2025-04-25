# サンプルのミニバッチを反復処理し、分類器を更新する

```python
# 分類器に 1000 個の文書のミニバッチを供給します。これは、いつでもメモリに最大 1000 個の文書があることを意味します。文書バッチが小さいほど、部分的なフィットメソッドの相対的なオーバーヘッドが大きくなります。
minibatch_size = 1000

# ルイト社の SGML ファイルを解析し、文書をストリームとして反復処理する data_stream を作成します。
minibatch_iterators = iter_minibatches(data_stream, minibatch_size)
total_vect_time = 0.0

# メインループ：サンプルのミニバッチを反復処理する
for i, (X_train_text, y_train) in enumerate(minibatch_iterators):
    tick = time.time()
    X_train = vectorizer.transform(X_train_text)
    total_vect_time += time.time() - tick

    for cls_name, cls in partial_fit_classifiers.items():
        tick = time.time()
        # 現在のミニバッチのサンプルで推定器を更新する
        cls.partial_fit(X_train, y_train, classes=all_classes)

        # テスト精度の統計を蓄積する
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
