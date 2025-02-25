# バイトオーダーの問題の対処

異なるバイトオーダーのマシンで作成されたデータを扱う際、バイトオーダーの問題に遭遇することがあります。Pandas に渡す前に、データをネイティブシステムのバイトオーダーに変換してください。

```python
x = np.array(list(range(10)), ">i4")  # big endian
newx = x.byteswap().newbyteorder()  # force native byteorder
s = pd.Series(newx)
```
