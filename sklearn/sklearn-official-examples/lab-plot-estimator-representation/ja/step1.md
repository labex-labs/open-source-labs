# コンパクトなテキスト表現

推定器を表示する最初の方法は、コンパクトなテキスト表現を通じるものです。推定器は、文字列として表示される場合、デフォルト以外の値に設定されたパラメータのみを表示します。これにより、視覚的なノイズが低減され、インスタンスを比較する際の違いを見つけやすくなります。

```python
from sklearn.linear_model import LogisticRegression

# l1ペナルティを持つロジスティック回帰のインスタンスを作成する
lr = LogisticRegression(penalty="l1")

# 推定器を表示する
print(lr)
```
