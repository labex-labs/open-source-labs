# Criando um DataFrame

A outra estrutura de dados fundamental é o DataFrame. É uma estrutura de dados rotulada bidimensional com colunas de tipos potencialmente diferentes.

```python
# Create a DataFrame
df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
```
