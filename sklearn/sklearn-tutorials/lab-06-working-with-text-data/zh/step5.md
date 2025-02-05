# 评估模型

为了评估我们模型的性能，我们可以使用一个留出的测试集。我们可以使用与训练集相同的过程来加载测试集。

```python
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
```

现在我们可以对测试集进行预处理并提取特征向量。

```python
X_test_counts = count_vect.transform(twenty_test.data)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)
```

最后，我们可以使用训练好的模型对测试集进行预测并计算准确率。

```python
predicted = clf.predict(X_test_tfidf)
accuracy = np.mean(predicted == twenty_test.target)
```
