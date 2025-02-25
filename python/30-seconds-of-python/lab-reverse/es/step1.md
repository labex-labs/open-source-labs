# Función para invertir una lista

Escribe una función de Python llamada `reverse(itr)` que tome una lista o una cadena como argumento y devuelva una nueva lista o cadena que contenga los elementos o caracteres en orden inverso.

Tu función debe cumplir con los siguientes requisitos:

- La función debe llamarse `reverse`
- La función debe tomar un solo argumento, que es una lista o una cadena
- La función debe devolver una nueva lista o cadena que contenga los elementos o caracteres en orden inverso
- La función no debe modificar la lista o cadena original

```python
def reverse(itr):
  return itr[::-1]
```

```python
reverse([1, 2, 3]) # [3, 2, 1]
reverse('snippet') # 'teppins'
```
