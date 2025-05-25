# Inserir Dados Ausentes

Aqui, veremos como inserir valores ausentes em nossos dados.

```python
# Insert missing values
s = pd.Series([1., 2., 3.])
s.loc[0] = None
```
