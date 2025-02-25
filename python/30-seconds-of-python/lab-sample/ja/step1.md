# リスト内のランダムな要素

引数としてリストを受け取り、そのリストからランダムな要素を返す `random_element(lst)` 関数を書きなさい。

- `random.choice()` を使って、`lst` からランダムな要素を取得します。

```python
from random import choice

def sample(lst):
  return choice(lst)
```

```python
sample([3, 7, 9, 11]) # 9
```
