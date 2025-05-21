# Melhorando a Representação de Objetos

Nossa classe `Structure` é útil para criar e acessar objetos. No entanto, ela atualmente não tem uma boa maneira de se representar como uma string. Quando você imprime um objeto ou o visualiza no interpretador Python, você quer ver uma exibição clara e informativa. Isso ajuda você a entender o que o objeto é e quais são seus valores.

## Compreendendo a Representação de Objetos em Python

Em Python, existem dois métodos especiais que são usados para representar objetos de diferentes maneiras. Esses métodos são importantes porque permitem que você controle como seus objetos são exibidos.

- `__str__` - Este método é usado pela função `str()` e pela função `print()`. Ele fornece uma representação legível por humanos do objeto. Por exemplo, se você tiver um objeto `Stock`, o método `__str__` pode retornar algo como "Stock: GOOG, 100 shares at $490.1".
- `__repr__` - Este método é usado pelo interpretador Python e pela função `repr()`. Ele fornece uma representação mais técnica e inequívoca do objeto. O objetivo de `__repr__` é fornecer uma string que possa ser usada para recriar o objeto. Por exemplo, para um objeto `Stock`, ele pode retornar "Stock('GOOG', 100, 490.1)".

Vamos adicionar um método `__repr__` à nossa classe `Structure`. Isso tornará mais fácil depurar nosso código porque podemos ver claramente o estado de nossos objetos.

## Implementando uma Boa Representação

Agora, você precisa atualizar seu arquivo `structure.py`. Você adicionará o método `__repr__` à classe `Structure`. Este método criará uma string que representa o objeto de uma forma que pode ser usada para recriá-lo.

```python
def __repr__(self):
    """
    Return a representation of the object that can be used to recreate it.
    Example: Stock('GOOG', 100, 490.1)
    """
    # Get the class name
    cls_name = type(self).__name__

    # Get all the field values
    values = [getattr(self, name) for name in self._fields]

    # Format the fields and values
    args_str = ', '.join(repr(value) for value in values)

    # Return the formatted string
    return f"{cls_name}({args_str})"
```

Aqui está o que este método faz passo a passo:

1.  Ele obtém o nome da classe usando `type(self).__name__`. Isso é importante porque informa que tipo de objeto você está lidando.
2.  Ele recupera todos os valores dos campos da instância. Isso fornece os dados que o objeto contém.
3.  Ele cria uma representação de string com o nome da classe e os valores. Essa string pode ser usada para recriar o objeto.

## Testando a Representação Melhorada

Vamos testar nossa implementação aprimorada. Crie um novo arquivo chamado `test_repr.py`. Este arquivo criará algumas instâncias de nossas classes e imprimirá suas representações.

```python
# test_repr.py
from structure import Stock, Point, Date

# Create instances
s = Stock('GOOG', 100, 490.1)
p = Point(3, 4)
d = Date(2023, 11, 9)

# Print the representations
print(repr(s))
print(repr(p))
print(repr(d))

# Direct printing also uses __repr__ in the interpreter
print(s)
print(p)
print(d)
```

Para executar o teste, abra seu terminal e digite o seguinte comando:

```bash
python3 test_repr.py
```

Você deve ver a seguinte saída:

```
Stock('GOOG', 100, 490.1)
Point(3, 4)
Date(2023, 11, 9)
Stock('GOOG', 100, 490.1)
Point(3, 4)
Date(2023, 11, 9)
```

Esta saída é muito mais informativa do que antes. Quando você vê `Stock('GOOG', 100, 490.1)`, você sabe imediatamente o que o objeto representa. Você pode até copiar esta string e usá-la para recriar o objeto em seu código.

## O Benefício de Boas Representações

Uma boa implementação de `__repr__` é muito útil para depuração. Quando você está olhando para objetos no interpretador ou registrando-os durante a execução do programa, uma representação clara facilita a identificação de problemas rapidamente. Você pode ver o estado exato do objeto e entender o que pode estar dando errado.
