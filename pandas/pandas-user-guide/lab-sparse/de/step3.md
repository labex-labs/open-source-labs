# Das Verständnis von SparseDtype

Der `SparseDtype` speichert den Datentyp der nicht-spärren Werte und den skalaren Füllwert. Wir können ihn erstellen, indem wir nur einen Datentyp übergeben oder auch einen expliziten Füllwert.

```python
# Creating a SparseDtype
print(pd.SparseDtype(np.dtype('datetime64[ns]')))

# Creating a SparseDtype with an explicit fill value
print(pd.SparseDtype(np.dtype('datetime64[ns]'), fill_value=pd.Timestamp('2017-01-01')))
```
