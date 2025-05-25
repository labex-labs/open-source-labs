# Criando um Record Array

Um record array é uma subclasse de ndarray que permite o acesso aos campos por atributo em vez de índice. Podemos criar um record array usando a função `np.rec.array`.

```python
# Create a record array
recordarr = np.rec.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```
