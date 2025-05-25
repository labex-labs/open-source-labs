# Escolhendo Colunas

O argumento `usecols` é usado para selecionar quais colunas importar. Ele aceita um único inteiro ou uma sequência de inteiros correspondentes aos índices das colunas a serem importadas.

```python
np.genfromtxt(StringIO(data), usecols=(0, -1))
```
