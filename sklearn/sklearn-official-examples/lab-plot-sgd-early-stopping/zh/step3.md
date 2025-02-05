# 训练和评估估计器

下一步是使用每种停止标准来训练和评估估计器。我们将使用一个循环来遍历每个估计器和停止标准，并且使用另一个循环来遍历不同的最大迭代次数。然后，我们会将结果存储在一个 pandas 数据框中以便于绘图。

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

# 将结果转换为 pandas 数据框以便于绘图
columns = [
    "停止标准",
    "max_iter",
    "拟合时间（秒）",
    "n_iter_",
    "训练分数",
    "测试分数",
]
results_df = pd.DataFrame(results, columns=columns)
```
