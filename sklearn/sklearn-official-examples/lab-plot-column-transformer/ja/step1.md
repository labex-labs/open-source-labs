# データセット

20のトピックに関するニュースグループの投稿から構成される20ニュースグループデータセットを使用します。このデータセットは、特定の日付の前後に投稿されたメッセージに基づいて学習用とテスト用のサブセットに分割されます。実行時間を短縮するため、2つのカテゴリの投稿のみを使用します。

```python
categories = ["sci.med", "sci.space"]
X_train, y_train = fetch_20newsgroups(
    random_state=1,
    subset="train",
    categories=categories,
    remove=("footers", "quotes"),
    return_X_y=True,
)
X_test, y_test = fetch_20newsgroups(
    random_state=1,
    subset="test",
    categories=categories,
    remove=("footers", "quotes"),
    return_X_y=True,
)
```
