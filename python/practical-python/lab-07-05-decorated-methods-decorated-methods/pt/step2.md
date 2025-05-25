# Métodos Estáticos

`@staticmethod` é usado para definir os chamados métodos de classe _estáticos_ (do C++/Java). Um método estático é uma função que faz parte da classe, mas que _não_ opera em instâncias.

```python
class Foo(object):
    @staticmethod
    def bar(x):
        print('x =', x)

>>> Foo.bar(2) # x=2
>>>
```

Métodos estáticos são, por vezes, usados para implementar código de suporte interno para uma classe. Por exemplo, código para ajudar a gerenciar instâncias criadas (gerenciamento de memória, recursos do sistema, persistência, bloqueio, etc.). Eles também são usados por certos padrões de projeto (não discutidos aqui).
