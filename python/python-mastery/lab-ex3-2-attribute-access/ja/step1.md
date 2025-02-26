# 3つの操作

Pythonのオブジェクトシステム全体は、たった3つのコア操作で構成されています。属性の取得、設定、削除です。通常は、次のようにドット (.) を使ってアクセスします。

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name    # 取得
'GOOG'
>>> s.shares = 50    # 設定
>>> del s.shares     # 削除
>>>
```

これら3つの操作は、関数としても利用できます。たとえば：

```python
>>> getattr(s, 'name')            # s.name と同じ
'GOOG'
>>> setattr(s,'shares', 50)      # s.shares = 50 と同じ
>>> delattr(s,'shares')          # del s.shares と同じ
>>>
```

属性の存在を調べるために、追加の関数 `hasattr()` を使うことができます。

```python
>>> hasattr(s, 'name')
True
>>> hasattr(s, 'blah')
False
>>>
```
