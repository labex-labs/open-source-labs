# String Representation

Each character in a string is stored internally as a so-called Unicode "code-point" which is
an integer. You can specify an exact code-point value using the following escape sequences:

```python
a = '\xf1'          # a = 'ñ'
b = '\u2200'        # b = '∀'
c = '\U0001D122'    # c = '𝄢'
d = '\N{FOR ALL}'   # d = '∀'
```

The [Unicode Character Database](https://unicode.org/charts) is a reference for all
available character codes.
