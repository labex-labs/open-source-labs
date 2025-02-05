# 生产者 - 消费者问题

生成器与各种形式的**生产者 - 消费者**问题密切相关。

```python
# 生产者
def follow(f):
 ...
    while True:
     ...
        yield line        # 生成下方 `line` 中的值
     ...

# 消费者
for line in follow(f):    # 消费上方 `yield` 产生的值
 ...
```

`yield` 产生值，`for` 循环消费这些值。
