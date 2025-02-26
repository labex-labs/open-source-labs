# あらゆる場所での反復処理

多くの異なるオブジェクトが反復処理をサポートしています。

```python
a = 'hello'
for c in a: # a の文字をループ処理する
 ...

b = { 'name': 'Dave', 'password':'foo'}
for k in b: # 辞書のキーをループ処理する
 ...

c = [1,2,3,4]
for i in c: # リスト/タプルの要素をループ処理する
 ...

f = open('foo.txt')
for x in f: # ファイルの行をループ処理する
 ...
```
