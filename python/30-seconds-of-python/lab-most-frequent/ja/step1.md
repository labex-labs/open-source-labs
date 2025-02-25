# 最も頻繁に出現する要素

整数のリストを入力として受け取り、そのリストの中で最も頻繁に出現する要素を返す `most_frequent(lst)` というPython関数を書きます。同じ回数だけ出現し、最も高い頻度を持つ複数の要素がある場合、リストで最初に現れる要素を返します。

この問題を解決するには、次の手順に従うことができます。

1. `set()` を使用して、`lst` の一意の値を取得します。
2. `max()` を使用して、最も多く出現する要素を見つけます。

あなたの関数は次のシグネチャを持つ必要があります。

```python
def most_frequent(lst: List[int]) -> int:
```

```python
def most_frequent(lst):
  return max(set(lst), key = lst.count)
```

```python
most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]) #2
```
