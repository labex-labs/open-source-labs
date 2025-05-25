# Exercício 7.8: Simplificando Chamadas de Funções

No exemplo acima, os usuários podem achar chamadas como `typedproperty('shares', int)` um pouco verbosas para digitar - especialmente se forem repetidas muitas vezes. Adicione as seguintes definições ao arquivo `typedproperty.py`:

```python
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
```

Agora, reescreva a classe `Stock` para usar essas funções em vez disso:

```python
class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Ah, isso é um pouco melhor. A principal conclusão aqui é que closures (fechamentos) e `lambda` podem frequentemente ser usados para simplificar o código e eliminar repetições irritantes. Isso geralmente é bom.
