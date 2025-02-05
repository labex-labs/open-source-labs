# 总结

在本实验中，我们通过比较两种方法（“特征哈希器（FeatureHasher）”和“字典向量化器（DictVectorizer）”）以及四种专用文本向量化器（“计数向量化器（CountVectorizer）”、“哈希向量化器（HashingVectorizer）”和“词频 - 逆文档频率向量化器（TfidfVectorizer）”）来探索文本向量化。我们对这些向量化方法进行了基准测试并绘制了结果。我们得出结论，“哈希向量化器（HashingVectorizer）”的性能优于“计数向量化器（CountVectorizer）”，但其代价是由于哈希冲突导致转换的不可逆性。此外，在手动分词的文档上，“字典向量化器（DictVectorizer）”和“特征哈希器（FeatureHasher）”比它们对应的文本向量化器表现更好，因为前一种向量化器的内部分词步骤会编译一次正则表达式，然后在所有文档中重复使用它。
