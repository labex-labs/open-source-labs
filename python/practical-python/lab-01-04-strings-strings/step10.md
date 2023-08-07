# Raw Strings

Raw strings are string literals with an uninterpreted backslash. They are specified by prefixing the initial quote with a lowercase "r".

```python
>>> rs = r'c:\newdata\test' # Raw (uninterpreted backslash)
>>> rs
'c:\\newdata\\test'
```

The string is the literal text enclosed inside, exactly as typed. This is useful in situations where the backslash has special significance. Example: filename, regular expressions, etc.
