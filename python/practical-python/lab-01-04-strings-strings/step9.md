# Byte Strings

A string of 8-bit bytes, commonly encountered with low-level I/O, is written as follows:

```python
data = b'Hello World\r\n'
```

By putting a little b before the first quotation, you specify that it is a byte string as opposed to a text string.

Most of the usual string operations work.

```python
len(data)                         # 13
data[0:5]                         # b'Hello'
data.replace(b'Hello', b'Cruel')  # b'Cruel World\r\n'
```

Indexing is a bit different because it returns byte values as integers.

```python
data[0]   # 72 (ASCII code for 'H')
```

Conversion to/from text strings.

```python
text = data.decode('utf-8') # bytes -> text
data = text.encode('utf-8') # text -> bytes
```

The `'utf-8'` argument specifies a character encoding. Other common values include `'ascii'` and `'latin1'`.
