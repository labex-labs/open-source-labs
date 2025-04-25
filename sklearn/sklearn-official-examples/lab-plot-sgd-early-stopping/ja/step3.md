# 推定器を学習して評価する

次のステップは、各停止基準を使用して推定器を学習して評価することです。各推定器と停止基準を反復処理するためのループを使用し、さらに別のループを使用して異なる最大反復回数を反復処理します。その後、結果を簡単にプロットするために pandas のデータフレームに格納します。

```python
results = []
for estimator_name, estimator in estimator_dict.items():
    print(estimator_name + ": ", end="")
    for max_iter in range(1, 50):
        print(".", end="")
        sys.stdout.flush()

        fit_time, n_iter, train_score, test_score = fit_and_score(
            estimator, max_iter, X_train, X_test, y_train, y_test
        )

        results.append(
            (estimator_name, max_iter, fit_time, n_iter, train_score, test_score)
        )
    print("")

# 結果を簡単にプロットするために pandas のデータフレームに変換する
columns = [
    "停止基準",
    "max_iter",
    "学習時間 (秒)",
    "n_iter_",
    "トレーニングスコア",
    "テストスコア",
]
results_df = pd.DataFrame(results, columns=columns)
```
