# 文字列メソッド

文字列には、文字列データに対して様々な操作を行うメソッドがあります。

例：先頭と末尾の空白を取り除く。

```python
s =' Hello '
t = s.strip()     # 'Hello'
```

例：ケース変換。

```python
s = 'Hello'
l = s.lower()     # 'hello'
u = s.upper()     # 'HELLO'
```

例：テキストの置換。

```python
s = 'Hello world'
t = s.replace('Hello ','Hallo')   # 'Hallo world'
```

**その他の文字列メソッド**：

文字列には、テキストデータをテストおよび操作するためのさまざまな他のメソッドがあります。これはメソッドの小さなサンプルです：

```python
s.endswith(suffix)     # 文字列がsuffixで終わるかどうかをチェックする
s.find(t)              # sの中でtが最初に出現する位置
s.index(t)             # sの中でtが最初に出現する位置
s.isalpha()            # 文字がアルファベットかどうかをチェックする
s.isdigit()            # 文字が数字かどうかをチェックする
s.islower()            # 文字が小文字かどうかをチェックする
s.isupper()            # 文字が大文字かどうかをチェックする
s.join(slist)          # sを区切り文字として文字列のリストを結合する
s.lower()              # 小文字に変換する
s.replace(old,new)     # テキストを置換する
s.rfind(t)             # 文字列の末尾からtを検索する
s.rindex(t)            # 文字列の末尾からtを検索する
s.split([delim])       # 文字列を部分文字列のリストに分割する
s.startswith(prefix)   # 文字列がprefixで始まるかどうかをチェックする
s.strip()              # 先頭と末尾の空白を取り除く
s.upper()              # 大文字に変換する
```
