# 数値正規化ベクトル化器の定義

先ほど定義した`number_normalizer()`関数を使用するトークナイザを構築するため、`TfidfVectorizer()`から継承する`NumberNormalizingVectorizer()`クラスを定義します。

```python
class NumberNormalizingVectorizer(TfidfVectorizer):
    def build_tokenizer(self):
        tokenize = super().build_tokenizer()
        return lambda doc: list(number_normalizer(tokenize(doc)))
```
