# 再訪：例外処理

演習では、次のような関数 `parse()` を書きました。

```python
# fileparse.py
def parse(f, types=None, names=None, delimiter=None):
    records = []
    for line in f:
        line = line.strip()
        if not line: continue
        try:
            records.append(split(line,types,names,delimiter))
        except ValueError as e:
            print("Couldn't parse :", line)
            print("Reason :", e)
    return records
```

`try-except` 文に注目してください。`except` ブロックで何をすべきでしょうか？

警告メッセージを表示するべきですか？

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    print("Couldn't parse :", line)
    print("Reason :", e)
```

それとも、黙って無視しますか？

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    pass
```

どちらの解決策も満足のいくものではありません。なぜなら、多くの場合、両方の動作（ユーザーが選択可能）が必要だからです。
