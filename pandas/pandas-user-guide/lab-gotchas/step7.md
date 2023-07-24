# Handling Byte-ordering Issues

You may encounter byte-ordering issues when dealing with data created on a machine with a different byte order. Convert the data to the native system byte order before passing it to Pandas.

```python
x = np.array(list(range(10)), ">i4")  # big endian
newx = x.byteswap().newbyteorder()  # force native byteorder
s = pd.Series(newx)
```
