# リストの反復処理と検索

`for` を使用して、リストの内容を反復処理します。

```python
for name in names:
    # name を使用する
    # たとえば、print(name)
   ...
```

これは、他のプログラミング言語の `foreach` 文に似ています。

何かの位置を迅速に見つけるには、`index()` を使用します。

```python
names = ['Elwood','Jake','Curtis']
names.index('Curtis')   # 2
```

要素が複数回登場する場合、`index()` は最初の出現箇所のインデックスを返します。

要素が見つからない場合、`ValueError` 例外が発生します。
