# Aplicando Decoradores via Herança

Na Etapa 2, criamos um decorador de classe que simplifica nosso código. Um decorador de classe é um tipo especial de função que recebe uma classe como argumento e retorna uma classe modificada. É uma ferramenta útil em Python para adicionar funcionalidade às classes sem modificar seu código original. No entanto, ainda precisamos aplicar explicitamente o decorador `@validate_attributes` a cada classe. Isso significa que toda vez que criarmos uma nova classe que precise de validação, teremos que nos lembrar de adicionar este decorador, o que pode ser um pouco complicado.

Podemos melhorar isso ainda mais aplicando o decorador automaticamente através da herança. Herança é um conceito fundamental em programação orientada a objetos, onde uma subclasse pode herdar atributos e métodos de uma classe pai. O método `__init_subclass__` do Python foi introduzido no Python 3.6 para permitir que as classes pai personalizem a inicialização das subclasses. Isso significa que, quando uma subclasse é criada, a classe pai pode realizar algumas ações sobre ela. Podemos usar esse recurso para aplicar automaticamente nosso decorador a qualquer classe que herde de `Structure`.

Vamos implementar isso:

1. Abra o arquivo `structure.py` no seu editor. Este arquivo contém a definição da classe `Structure`, e vamos modificá-lo para usar o método `__init_subclass__`.

2. Adicione o método `__init_subclass__` à classe `Structure`:

```python
class Structure:
    _fields = ()
    _types = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f'{type(self).__name__}({values})'

    @classmethod
    def create_init(cls):
        '''
        Create an __init__ method from _fields
        '''
        body = 'def __init__(self, %s):\n' % ', '.join(cls._fields)
        for name in cls._fields:
            body += f'    self.{name} = {name}\n'

        # Execute the function creation code
        namespace = {}
        exec(body, namespace)
        setattr(cls, '__init__', namespace['__init__'])

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

O método `__init_subclass__` é um método de classe, o que significa que ele pode ser chamado na própria classe, em vez de em uma instância da classe. Quando uma subclasse de `Structure` é criada, este método será chamado automaticamente. Dentro deste método, chamamos o decorador `validate_attributes` na subclasse `cls`. Dessa forma, toda subclasse de `Structure` terá automaticamente o comportamento de validação.

3. Salve o arquivo.

Após fazer alterações no arquivo `structure.py`, precisamos salvá-lo para que as alterações sejam aplicadas.

4. Agora, vamos atualizar nosso arquivo `stock.py` para aproveitar este novo recurso. Abra o arquivo `stock.py` no seu editor para modificá-lo. Este arquivo contém a definição da classe `Stock`, e vamos fazê-la herdar da classe `Structure` para usar a aplicação automática do decorador.

5. Modifique o arquivo `stock.py` para remover o decorador explícito:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Note que nós:

- Removemos a importação `validate_attributes` porque não precisamos mais importá-la explicitamente, já que o decorador é aplicado automaticamente através da herança.
- Removemos o decorador `@validate_attributes` porque o método `__init_subclass__` na classe `Structure` cuidará de aplicá-lo.
- O código agora depende apenas da herança de `Structure` para obter o comportamento de validação.

6. Execute os testes novamente para verificar se tudo ainda funciona:

```bash
cd ~/project
python3 teststock.py
```

Executar os testes é importante para garantir que nossas alterações não quebraram nada. Se todos os testes passarem, significa que a aplicação automática do decorador através da herança está funcionando corretamente.

Você deverá ver todos os testes passando:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Vamos testar nossa classe `Stock` novamente para garantir que ela funcione como esperado:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Este comando cria uma instância da classe `Stock` e imprime sua representação e o custo. Se a saída for a esperada, significa que a classe `Stock` está funcionando corretamente com a aplicação automática do decorador.

Saída:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Esta implementação é ainda mais limpa! Ao usar `__init_subclass__`, eliminamos a necessidade de aplicar decoradores explicitamente. Qualquer classe que herde de `Structure` obtém automaticamente o comportamento de validação.
