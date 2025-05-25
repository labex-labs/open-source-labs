# Mutação com Métodos de Funções Definidas pelo Usuário (UDF)

Ao usar um método pandas que recebe uma UDF, evite alterar o DataFrame dentro da UDF. Em vez disso, faça uma cópia antes de fazer as alterações.

```python
def f(s):
    s = s.copy()
    s.pop("a")
    return s

df = pd.DataFrame({"a": [1, 2, 3], 'b': [4, 5, 6]})
df.apply(f, axis="columns")
```
