# Definindo o Tipo de Dados

O argumento `dtype` é usado para controlar como as strings são convertidas para outros tipos. Ele pode ser um único tipo, uma sequência de tipos, uma string separada por vírgulas, um dicionário, uma sequência de tuplas, um objeto `numpy.dtype` existente ou `None` para determinar o tipo a partir dos próprios dados.

```python
np.genfromtxt(StringIO(data), dtype=float)
```
