# 设置向量化器并留出测试集

```python
# 创建向量化器并将特征数量限制在合理的最大值
vectorizer = HashingVectorizer(decode_error="ignore", n_features=2**18, alternate_sign=False)

# 遍历解析后的路透社 SGML 文件的迭代器。
data_stream = stream_reuters_documents()

# 我们学习“acq”类与其他所有类之间的二分类。
# 选择“acq”是因为它在路透社文件中分布大致均匀。对于其他数据集，应该注意创建一个包含实际比例正例的测试集。
all_classes = np.array([0, 1])
positive_class = "acq"

# 这里有一些支持 `partial_fit` 方法的分类器
partial_fit_classifiers = {
    "SGD": SGDClassifier(max_iter=5),
    "Perceptron": Perceptron(),
    "NB Multinomial": MultinomialNB(alpha=0.01),
    "Passive-Aggressive": PassiveAggressiveClassifier(),
}

# 测试数据统计信息
test_stats = {"n_test": 0, "n_test_pos": 0}

# 首先我们留出一些示例来估计准确率
n_test_documents = 1000
X_test_text, y_test = get_minibatch(data_stream, 1000)
X_test = vectorizer.transform(X_test_text)
test_stats["n_test"] += len(y_test)
test_stats["n_test_pos"] += sum(y_test)
print("Test set is %d documents (%d positive)" % (len(y_test), sum(y_test)))
```
