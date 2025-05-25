# Acesso a Campos (Field Access)

Se o objeto ndarray for um array estruturado, os campos do array podem ser acessados indexando o array com strings, como um dicionário.

```python
x = np.array([(1, 2), (3, 4), (5, 6)], dtype=[('a', np.int32), ('b', np.int32)])
print(x['a'])  # Output: [1, 3, 5]
```
