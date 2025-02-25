# リストをシャッフルする

入力としてリストを受け取り、同じ項目をランダムな順序で含む新しいリストを返す関数 `shuffle(lst)` を書きます。関数は、Fisher-Yates アルゴリズムを使用してリスト内の項目をシャッフルする必要があります。

Fisher-Yates アルゴリズムは以下のように機能します。

1. リストの最後の項目から始めます。
2. 0 から現在のインデックスまでのランダムなインデックスを生成します。
3. 現在のインデックスにある項目とランダムなインデックスにある項目を交換します。
4. リストの次の項目に移動し、すべての項目がシャッフルされるまで 2-3 の手順を繰り返します。

関数は元のリストを変更してはいけません。代わりに、シャッフルされた項目を含む新しいリストを作成する必要があります。

入力リストには少なくとも 1 つの項目が含まれていると仮定して構いません。

```python
from copy import deepcopy
from random import randint

def shuffle(lst):
  temp_lst = deepcopy(lst)
  m = len(temp_lst)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  return temp_lst
```

```python
foo = [1, 2, 3]
shuffle(foo) # [2, 3, 1], foo = [1, 2, 3]
```
