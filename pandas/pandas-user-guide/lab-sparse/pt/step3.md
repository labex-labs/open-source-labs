# Entendendo `SparseDtype`

O `SparseDtype` armazena o `dtype` dos valores não esparsos e o valor de preenchimento escalar. Podemos construí-lo passando apenas um `dtype`, ou também um valor de preenchimento explícito.

```python
# Creating a SparseDtype
print(pd.SparseDtype(np.dtype('datetime64[ns]')))

# Creating a SparseDtype with an explicit fill value
print(pd.SparseDtype(np.dtype('datetime64[ns]'), fill_value=pd.Timestamp('2017-01-01')))
```
