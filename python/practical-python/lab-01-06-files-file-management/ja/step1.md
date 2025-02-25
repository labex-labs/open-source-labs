# ファイル入出力

ファイルを開く。

```python
f = open('foo.txt', 'rt')     # 読み込み用に開く (テキスト)
g = open('bar.txt', 'wt')     # 書き込み用に開く (テキスト)
```

すべてのデータを読み込む。

```python
data = f.read()

# 最大'maxbytes' バイトまで読み込む
data = f.read([maxbytes])
```

いくつかのテキストを書き込む。

```python
g.write('some text')
```

終了したら閉じる。

```python
f.close()
g.close()
```

ファイルは適切に閉じる必要がありますが、忘れるのは簡単なことです。したがって、好ましい方法は、次のように `with` ステートメントを使用することです。

```python
with open(filename, 'rt') as file:
    # ファイル `file` を使用する
  ...
    # 明示的に閉じる必要はない
...文
```

これは、制御がインデントされたコードブロックを離れるときに自動的にファイルを閉じます。
