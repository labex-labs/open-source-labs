# Distancia de Hamming

Escribe una función `hamming_distance(a, b)` que tome dos enteros como argumentos y devuelva la distancia de Hamming entre ellos. La función debe realizar los siguientes pasos:

1. Utiliza el operador XOR (`^`) para encontrar la diferencia de bits entre los dos números.
2. Utiliza `bin()` para convertir el resultado a una cadena binaria.
3. Convierte la cadena a una lista y utiliza `count()` de la clase `str` para contar y devolver el número de `1`s en ella.

```python
def hamming_distance(a, b):
  return bin(a ^ b).count('1')
```

```python
hamming_distance(2, 3) # 1
```
