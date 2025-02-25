# Mediana

Escribe una función de Python llamada `find_median` que tome una lista de números como argumento y devuelva la mediana de la lista. Tu función debe realizar los siguientes pasos:

1. Ordena los números de la lista utilizando `list.sort()`.
2. Encuentra la mediana, que es el elemento central de la lista si la longitud de la lista es impar o el promedio de los dos elementos centrales si la longitud de la lista es par.
3. Devuelve la mediana.

Tu función no debe utilizar ninguna librería o función integrada de Python que resuelva directamente el problema.

```python
def median(list):
  list.sort()
  list_length = len(list)
  if list_length % 2 == 0:
    return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2
  return float(list[int(list_length / 2)])
```

```python
median([1, 2, 3]) # 2.0
median([1, 2, 3, 4]) # 2.5
```
