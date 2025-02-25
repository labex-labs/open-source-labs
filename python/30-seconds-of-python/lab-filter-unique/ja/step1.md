# 一意のリスト値をフィルタリングする

`filter_unique(lst)` という名前の Python 関数を書きます。この関数は、リストを引数として受け取り、非一意の値のみを含む新しいリストを返します。この問題を解くには、次の手順に従うことができます。

1. `collections.Counter` を使用して、リスト内の各値のカウントを取得します。
2. 非一意の値のみを含むリストを作成するために、リスト内包表記を使用します。

関数は次の要件を満たす必要があります。

- 関数はリストを引数として受け取る必要があります。
- 関数は非一意の値のみを含む新しいリストを返す必要があります。
- 関数は元のリストを変更してはなりません。
- 関数は大文字と小文字を区別します。つまり、'a' と 'A' は異なる値と見なされます。

```python
def filter_unique(lst):
    # ここにコードを記述してください
```

```python
from collections import Counter

def filter_unique(lst):
  return [item for item, count in Counter(lst).items() if count > 1]
```

```python
filter_unique([1, 2, 2, 3, 4, 4, 5]) # [2, 4]
```
