# 空值类型

```python
email_address = None
```

`None` 通常用作可选值或缺失值的占位符。在条件判断中，它被视为 `False`。

```python
if email_address:
    send_email(email_address, msg)
```
