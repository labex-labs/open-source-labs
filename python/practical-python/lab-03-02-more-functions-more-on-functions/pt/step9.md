# Variáveis Globais (Global Variables)

Funções podem acessar livremente os valores de variáveis globais definidas no mesmo arquivo.

```python
name = 'Dave'

def greeting():
    print('Hello', name)  # Usando a variável global `name`
```

No entanto, funções não podem modificar variáveis globais:

```python
name = 'Dave'

def spam():
  name = 'Guido'

spam()
print(name) # imprime 'Dave'
```

**Lembre-se: Todas as atribuições em funções são locais.**
