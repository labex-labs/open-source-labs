# Usando el acceso disperso

Podemos usar el accesor `.sparse` para obtener atributos y métodos específicos de datos dispersos.

```python
# Creando una Serie con valores dispersos
s = pd.Series([0, 0, 1, 2], dtype="Sparse[int]")

# Usando el accesor disperso
print(s.sparse.density)
print(s.sparse.fill_value)
```
