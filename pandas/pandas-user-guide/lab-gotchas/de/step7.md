# Das Umgang mit Byte-Reihenfolge-Problemen

Sie können bei der Bearbeitung von Daten, die auf einem Computer mit einer anderen Byte-Reihenfolge erstellt wurden, Probleme mit der Byte-Reihenfolge auftauchen. Konvertieren Sie die Daten in die native System-Byte-Reihenfolge, bevor Sie sie an Pandas übergeben.

```python
x = np.array(list(range(10)), ">i4")  # big endian
newx = x.byteswap().newbyteorder()  # force native byteorder
s = pd.Series(newx)
```
