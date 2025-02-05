# 创建转换器

我们将创建从数据集中提取特征的转换器。我们将定义两个执行数据转换的函数，然后使用 Scikit-Learn 的 `FunctionTransformer` 创建转换器。

```python
def subject_body_extractor(posts):
    # 构造一个具有两列的对象数据类型数组
    # 第一列 ='subject'，第二列 = 'body'
    features = np.empty(shape=(len(posts), 2), dtype=object)
    for i, text in enumerate(posts):
        # 临时变量 `_` 存储 '\n\n'
        headers, _, body = text.partition("\n\n")
        # 将正文文本存储在第二列
        features[i, 1] = body

        prefix = "Subject:"
        sub = ""
        # 将 'Subject:' 之后的文本保存在第一列
        for line in headers.split("\n"):
            if line.startswith(prefix):
                sub = line[len(prefix) :]
                break
        features[i, 0] = sub

    return features

subject_body_transformer = FunctionTransformer(subject_body_extractor)

def text_stats(posts):
    return [{"length": len(text), "num_sentences": text.count(".")} for text in posts]

text_stats_transformer = FunctionTransformer(text_stats)
```
