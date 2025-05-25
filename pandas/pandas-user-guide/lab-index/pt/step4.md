# Trabalhando com Dados Ausentes

Pandas fornece vários métodos para limpar dados e preencher valores ausentes.

```python
# Criando um DataFrame com valores ausentes
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]})

# Preenchendo valores ausentes
df.fillna(value=0, inplace=True)
```
