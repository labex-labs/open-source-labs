# 로깅 사용하기

`logging` 모듈은 이 문제를 해결할 수 있습니다.

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

코드는 경고 메시지 또는 특수한 `Logger` 객체를 발행하도록 수정되었습니다. `logging.getLogger(__name__)`으로 생성된 객체입니다.
