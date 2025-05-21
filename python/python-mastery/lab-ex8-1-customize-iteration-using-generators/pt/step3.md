# Aprimorando Classes com Recursos de Iteração

Agora, tornamos nossa classe `Structure` e suas subclasses compatíveis com iteração. Iteração é um conceito poderoso em Python que permite que você percorra uma coleção de itens um por um. Quando uma classe suporta iteração, ela se torna mais flexível e pode funcionar com muitos recursos embutidos do Python. Vamos explorar como esse suporte à iteração possibilita muitos recursos poderosos em Python.

## Aproveitando a Iteração para Conversões de Sequência

Em Python, existem funções embutidas como `list()` e `tuple()`. Essas funções são muito úteis porque podem receber qualquer objeto iterável como entrada. Um objeto iterável é algo que você pode percorrer em loop, como uma lista, uma tupla ou, agora, nossas instâncias da classe `Structure`. Como nossa classe `Structure` agora suporta iteração, podemos facilmente converter instâncias dela em listas ou tuplas.

1. Vamos tentar essas operações com uma instância `Stock`. A classe `Stock` é uma subclasse de `Structure`. Execute o seguinte comando em seu terminal:

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('As list:', list(s)); print('As tuple:', tuple(s))"
```

Este comando primeiro importa a classe `Stock`, cria uma instância dela e, em seguida, converte essa instância em uma lista e uma tupla usando as funções `list()` e `tuple()`, respectivamente. A saída mostrará a instância representada como uma lista e uma tupla:

```
As list: ['GOOG', 100, 490.1]
As tuple: ('GOOG', 100, 490.1)
```

## Desempacotamento (Unpacking)

Python tem um recurso muito útil chamado desempacotamento (unpacking). Desempacotamento permite que você pegue um objeto iterável e atribua seus elementos a variáveis individuais de uma só vez. Como nossa instância `Stock` é iterável, podemos usar esse recurso de desempacotamento nela.

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); name, shares, price = s; print(f'Name: {name}, Shares: {shares}, Price: {price}')"
```

Neste código, criamos uma instância `Stock` e, em seguida, desempacotamos seus elementos em três variáveis: `name`, `shares` e `price`. Em seguida, imprimimos essas variáveis. A saída mostrará os valores dessas variáveis:

```
Name: GOOG, Shares: 100, Price: 490.1
```

## Adicionando Recursos de Comparação

Quando uma classe suporta iteração, torna-se mais fácil implementar operações de comparação. Operações de comparação são usadas para verificar se dois objetos são iguais ou não. Vamos adicionar um método `__eq__()` à nossa classe `Structure` para comparar instâncias.

1. Abra o arquivo `structure.py` novamente. O método `__eq__()` é um método especial em Python que é chamado quando você usa o operador `==` para comparar dois objetos. Adicione o seguinte código à classe `Structure` no arquivo `structure.py`:

```python
def __eq__(self, other):
    return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

Este método primeiro verifica se o objeto `other` é uma instância da mesma classe que `self` usando a função `isinstance()`. Em seguida, ele converte tanto `self` quanto `other` em tuplas e verifica se essas tuplas são iguais.

O arquivo `structure.py` completo agora deve ser assim:

```python
class StructureMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = clsdict.get('_fields', [])
        for name in fields:
            clsdict[name] = property(lambda self, name=name: getattr(self, '_'+name))
        return super().__new__(cls, name, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)

    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

2. Depois de adicionar o método `__eq__()`, salve o arquivo `structure.py`.

3. Vamos testar a capacidade de comparação. Execute o seguinte comando em seu terminal:

```bash
python3 -c "from stock import Stock; a = Stock('GOOG', 100, 490.1); b = Stock('GOOG', 100, 490.1); c = Stock('AAPL', 200, 123.4); print(f'a == b: {a == b}'); print(f'a == c: {a == c}')"
```

Este código cria três instâncias `Stock`: `a`, `b` e `c`. Em seguida, ele compara `a` com `b` e `a` com `c` usando o operador `==`. A saída mostrará os resultados dessas comparações:

```
a == b: True
a == c: False
```

4. Agora, para garantir que tudo esteja funcionando corretamente, precisamos executar os testes unitários. Testes unitários são um conjunto de código que verifica se diferentes partes do seu programa estão funcionando conforme o esperado. Execute o seguinte comando em seu terminal:

```bash
python3 teststock.py
```

Se tudo estiver funcionando corretamente, você deverá ver uma saída indicando que os testes foram aprovados:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

Ao adicionar apenas dois métodos simples (`__iter__()` e `__eq__()`), aprimoramos significativamente nossa classe `Structure` com recursos que a tornam mais Pythonica e fácil de usar.
