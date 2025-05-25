# Criando Variáveis Dummy

Você pode criar variáveis dummy a partir de dados de string usando o método `get_dummies`.

```python
# create dummy variables
s = pd.Series(["a", "a|b", np.nan, "a|c"], dtype="string")
s.str.get_dummies(sep="|")
```
