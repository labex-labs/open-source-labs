# 로깅 기본 사항

로거 (logger) 객체를 생성합니다.

```python
log = logging.getLogger(name)   # name 은 문자열입니다.
```

로그 메시지 발행.

```python
log.critical(message [, args])
log.error(message [, args])
log.warning(message [, args])
log.info(message [, args])
log.debug(message [, args])
```

_각 메서드는 서로 다른 심각도 레벨을 나타냅니다._

이들은 모두 형식화된 로그 메시지를 생성합니다. `args`는 `%` 연산자와 함께 메시지를 생성하는 데 사용됩니다.

```python
logmsg = message % args # 로그에 기록됨
```
