# 遍历示例的小批量数据并更新分类器

```python
# 我们将为分类器提供包含 1000 个文档的小批量数据；这意味着我们在任何时候最多在内存中保留 1000 个文档。文档批次越小，部分拟合方法的相对开销就越大。
minibatch_size = 1000

# 创建解析路透社 SGML 文件并将文档作为流进行迭代的数据流。
minibatch_iterators = iter_minibatches(data_stream, minibatch_size)
total_vect_time = 0.0

# 主循环：遍历示例的小批量数据
for i, (X_train_text, y_train) in enumerate(minibatch_iterators):
    tick = time.time()
    X_train = vectorizer.transform(X_train_text)
    total_vect_time += time.time() - tick

    for cls_name, cls in partial_fit_classifiers.items():
        tick = time.time()
        # 使用当前小批量中的示例更新估计器
        cls.partial_fit(X_train, y_train, classes=all_classes)

        # 累积测试准确率统计信息
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
