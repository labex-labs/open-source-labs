# 日志记录基础

创建一个日志记录器对象。

```python
log = logging.getLogger(name)   # name 是一个字符串
```

发出日志消息。

```python
log.critical(message [, args])
log.error(message [, args])
log.warning(message [, args])
log.info(message [, args])
log.debug(message [, args])
```

_每个方法代表不同的严重级别。_

所有这些方法都会创建一个格式化的日志消息。`args` 与 `%` 运算符一起用于创建消息。

```python
logmsg = message % args # 写入日志
```
