# Понимание SparseDtype

`SparseDtype` хранит тип данных (`dtype`) неразреженных значений и скалярное значение-заполнитель. Его можно создать, передав только `dtype`, или также явное значение-заполнитель.

```python
# Creating a SparseDtype
print(pd.SparseDtype(np.dtype('datetime64[ns]')))

# Creating a SparseDtype with an explicit fill value
print(pd.SparseDtype(np.dtype('datetime64[ns]'), fill_value=pd.Timestamp('2017-01-01')))
```
