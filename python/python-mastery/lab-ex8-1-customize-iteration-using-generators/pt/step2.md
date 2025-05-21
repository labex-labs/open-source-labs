# Adicionando Iteração a Classes Personalizadas

Agora que você compreendeu os conceitos básicos de geradores, vamos usá-los para adicionar recursos de iteração a classes personalizadas. Em Python, se você deseja tornar uma classe iterável, precisa implementar o método especial `__iter__()`. Uma classe iterável permite que você percorra seus elementos, assim como você pode percorrer uma lista ou uma tupla. Este é um recurso poderoso que torna suas classes personalizadas mais flexíveis e fáceis de trabalhar.

## Compreendendo o Método `__iter__()`

O método `__iter__()` é uma parte crucial para tornar uma classe iterável. Ele deve retornar um objeto iterador. Um iterador é um objeto que pode ser iterado (percorrido em loop). Uma maneira simples e eficaz de conseguir isso é definindo `__iter__()` como uma função geradora. Uma função geradora usa a palavra-chave `yield` para produzir uma sequência de valores, um de cada vez. Cada vez que a instrução `yield` é encontrada, a função pausa e retorna o valor. Na próxima vez que o iterador for chamado, a função retoma de onde parou.

## Modificando a Classe Structure

Na configuração deste laboratório, fornecemos uma classe base `Structure`. Outras classes, como `Stock`, podem herdar desta classe `Structure`. Herança é uma maneira de criar uma nova classe que herda as propriedades e métodos de uma classe existente. Ao adicionar um método `__iter__()` à classe `Structure`, podemos tornar todas as suas subclasses iteráveis. Isso significa que qualquer classe que herde de `Structure` terá automaticamente a capacidade de ser percorrida em loop.

1. Abra o arquivo `structure.py` no WebIDE:

```bash
cd ~/project
```

Este comando altera o diretório de trabalho atual para o diretório `project`, onde o arquivo `structure.py` está localizado. Você precisa estar no diretório correto para acessar e modificar o arquivo.

2. Observe a implementação atual da classe `Structure`:

```python
class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)
```

A classe `Structure` possui uma lista `_fields` que armazena os nomes dos atributos. O método `__init__()` é o construtor da classe. Ele inicializa os atributos do objeto verificando se o número de argumentos passados é igual ao número de campos. Caso contrário, ele levanta um `TypeError`. Caso contrário, ele define os atributos usando a função `setattr()`.

3. Adicione um método `__iter__()` que produza cada valor de atributo em ordem:

```python
def __iter__(self):
    for name in self._fields:
        yield getattr(self, name)
```

Este método `__iter__()` é uma função geradora. Ele percorre a lista `_fields` e usa a função `getattr()` para obter o valor de cada atributo. A palavra-chave `yield` então retorna o valor um por um.

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
```

Esta classe `Structure` atualizada agora possui o método `__iter__()`, o que a torna e suas subclasses iteráveis.

4. Salve o arquivo.
   Depois de fazer alterações no arquivo `structure.py`, você precisa salvá-lo para que as alterações sejam aplicadas.

5. Agora, vamos testar a capacidade de iteração criando uma instância `Stock` e iterando sobre ela:

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('Iterating over Stock:'); [print(val) for val in s]"
```

Este comando cria uma instância da classe `Stock`, que herda da classe `Structure`. Em seguida, itera sobre a instância usando uma compreensão de lista e imprime cada valor.

Você deve ver uma saída como esta:

```
Iterating over Stock:
GOOG
100
490.1
```

Agora, qualquer classe que herde de `Structure` será automaticamente iterável, e a iteração produzirá os valores dos atributos na ordem definida pela lista `_fields`. Isso significa que você pode facilmente percorrer os atributos de qualquer subclasse de `Structure` sem ter que escrever código adicional para iteração.
