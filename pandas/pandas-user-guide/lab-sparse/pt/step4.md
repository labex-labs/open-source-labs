# Usando o Acessador Esparso

Podemos usar o acessador `.sparse` para obter atributos e métodos específicos para dados esparsos.

```python
# Creating a Series with sparse values
s = pd.Series([0, 0, 1, 2], dtype="Sparse[int]")

# Using the sparse accessor
print(s.sparse.density)
print(s.sparse.fill_value)
```
