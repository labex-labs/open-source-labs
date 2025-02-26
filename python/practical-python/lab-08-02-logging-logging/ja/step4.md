# ロギングの基本

ロガーオブジェクトを作成します。

```python
log = logging.getLogger(name)   # name は文字列
```

ログメッセージを発行します。

```python
log.critical(message [, args])
log.error(message [, args])
log.warning(message [, args])
log.info(message [, args])
log.debug(message [, args])
```

_各メソッドは、異なる重大度レベルを表します。_

すべてのメソッドは、フォーマットされたログメッセージを作成します。`args` は、メッセージを作成するために `%` 演算子とともに使用されます。

```python
logmsg = message % args # ログに書き込まれます
```
