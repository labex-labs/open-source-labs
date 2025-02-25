# Indexación con Iterador Plano

El atributo `x.flat` devuelve un iterador que se puede utilizar para iterar sobre todo el array en estilo C-contiguo. Este iterador también se puede indexar utilizando indexación básica o indexación avanzada.

```python
x = np.arange(10)
iterator = x.flat
print(iterator[1:5])  # Salida: [1, 2, 3, 4]
```
