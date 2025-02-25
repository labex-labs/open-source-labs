# Тип None

```python
email_address = None
```

`None` часто используется в качестве заполнителя для необязательного или отсутствующего значения. В условных выражениях оно оценивается как `False`.

```python
if email_address:
    send_email(email_address, msg)
```
