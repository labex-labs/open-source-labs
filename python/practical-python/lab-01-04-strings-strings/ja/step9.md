# バイト文字列

8 ビットのバイトの文字列は、低レベルの入出力で一般的に遭遇するもので、以下のように書かれます。

```python
data = b'Hello World\r\n'
```

最初の引用符の前に小文字の b を付けることで、通常のテキスト文字列とは対照的に、それがバイト文字列であることを指定します。

ほとんどの通常の文字列操作が機能します。

```python
len(data)                         # 13
data[0:5]                         # b'Hello'
data.replace(b'Hello', b'Cruel')  # b'Cruel World\r\n'
```

インデックス付けは少し異なります。なぜなら、それは整数としてバイト値を返すからです。

```python
data[0]   # 72 ('H'の ASCII コード)
```

テキスト文字列への変換とその逆変換。

```python
text = data.decode('utf-8') # バイト -> テキスト
data = text.encode('utf-8') # テキスト -> バイト
```

`'utf-8'` 引数は文字エンコーディングを指定します。他の一般的な値には `'ascii'` や `'latin1'` があります。
