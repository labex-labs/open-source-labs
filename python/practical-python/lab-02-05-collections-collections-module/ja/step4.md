# 例：履歴の保持

問題：最後の N 件の履歴を保持したい。解決策：`deque` を使用する。

```python
from collections import deque

history = deque(maxlen=N)
with open(filename) as f:
    for line in f:
        history.append(line)
     ...
```

`collections` モジュールは、集計やインデックス付けなどの特殊な目的のデータ処理問題を扱う際に最も便利なライブラリモジュールの 1 つかもしれません。

この演習では、いくつかの簡単な例を見てみましょう。まず、`report.py` プログラムを実行して、対話型モードで株式のポートフォリオを読み込んでください。

```bash
$ python3 -i report.py
```
