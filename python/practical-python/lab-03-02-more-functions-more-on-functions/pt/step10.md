# Modificando Globais (Globals)

Se você precisar modificar uma variável global, você deve declará-la como tal.

```python
name = 'Dave'

def spam():
    global name
    name = 'Guido' # Altera a variável global name acima
```

A declaração `global` deve aparecer antes de seu uso e a variável correspondente deve existir no mesmo arquivo que a função. Tendo visto isso, saiba que é considerado uma má prática. Na verdade, tente evitar `global` completamente, se possível. Se você precisar que uma função modifique algum tipo de estado fora da função, é melhor usar uma classe (mais sobre isso mais tarde).
