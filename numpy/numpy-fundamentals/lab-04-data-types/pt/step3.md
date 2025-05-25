# Recuperando o Tipo de Dados de um Array

Para determinar o tipo de dados de um array, você pode acessar o atributo `dtype`. Por exemplo:

```python
z.dtype
# returns the dtype of array z, which is uint8
```

O objeto `dtype` também contém informações sobre o tipo, como sua largura em bits e a ordem dos bytes. Você pode usar o objeto `dtype` para consultar propriedades do tipo, como se é um inteiro. Por exemplo:

```python
d = np.dtype(int)
# creates a dtype object for int

np.issubdtype(d, np.integer)
# returns True, indicating that d is a subdtype of np.integer

np.issubdtype(d, np.floating)
# returns False, indicating that d is not a subdtype of np.floating
```
