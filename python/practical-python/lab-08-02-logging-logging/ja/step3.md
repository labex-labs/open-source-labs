# logging の使用

`logging` モジュールを使うことでこの問題を解決できます。

```python
# fileparse.py
import logging
log = logging.getLogger(__name__)

def parse(f,types=None,names=None,delimiter=None):
 ...
    try:
        records.append(split(line,types,names,delimiter))
    except ValueError as e:
        log.warning("Couldn't parse : %s", line)
        log.debug("Reason : %s", e)
```

コードを修正して、警告メッセージを発行するか、特殊な `Logger` オブジェクトを使うようにしました。`logging.getLogger(__name__)` で作成されたものです。
