# 定义数字归一化矢量化器

我们将定义一个类 `NumberNormalizingVectorizer()`，它继承自 `TfidfVectorizer()`，以构建一个使用我们之前定义的 `number_normalizer()` 函数的分词器。

```python
class NumberNormalizingVectorizer(TfidfVectorizer):
    def build_tokenizer(self):
        tokenize = super().build_tokenizer()
        return lambda doc: list(number_normalizer(tokenize(doc)))
```
