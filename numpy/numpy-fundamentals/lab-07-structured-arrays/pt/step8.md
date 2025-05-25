# Convertendo um Structured Array para um Record Array

Podemos converter um structured array em um record array usando o método `view` e especificando o tipo `np.recarray`.

```python
# Convert a structured array to a record array
recordarr = x.view(np.recarray)
```
