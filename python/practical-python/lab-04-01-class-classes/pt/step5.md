# Métodos de Instância (Instance Methods)

Métodos de instância são funções aplicadas a instâncias de um objeto.

```python
class Player:
    ...
    # `move` é um método
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

O próprio objeto é sempre passado como o primeiro argumento.

```python
>>> a.move(1, 2)

# corresponde `a` a `self`
# corresponde `1` a `dx`
# corresponde `2` a `dy`
def move(self, dx, dy):
```

Por convenção, a instância é chamada de `self`. No entanto, o nome real usado não é importante. O objeto é sempre passado como o primeiro argumento. É apenas um estilo de programação Python chamar este argumento de `self`.
