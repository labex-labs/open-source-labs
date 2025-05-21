# Adicionando Conversões de Tipo

Nossa classe `MutInt` atualmente suporta operações de adição e comparação. No entanto, ela não funciona com as funções de conversão embutidas do Python, como `int()` e `float()`. Essas funções de conversão são muito úteis em Python. Por exemplo, quando você deseja converter um valor em um inteiro ou um número de ponto flutuante para diferentes cálculos ou operações, você confia nessas funções. Então, vamos adicionar as capacidades à nossa classe `MutInt` para trabalhar com elas.

1. Abra `mutint.py` no WebIDE e atualize-o com o seguinte código:

```python
# mutint.py

from functools import total_ordering

@total_ordering
class MutInt:
    """
    Uma classe de inteiro mutável que permite que seu valor seja modificado após a criação.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Inicializa com um valor inteiro."""
        self.value = value

    def __str__(self):
        """Retorna uma representação de string para impressão."""
        return str(self.value)

    def __repr__(self):
        """Retorna uma representação de string amigável para desenvolvedores."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Suporta formatação de string com especificações de formato."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Lida com a adição: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Lida com a adição invertida: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Lida com a adição in-place: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Lida com a comparação de igualdade: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Lida com a comparação menor que: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Converte para int."""
        return self.value

    def __float__(self):
        """Converte para float."""
        return float(self.value)

    __index__ = __int__  # Suporta indexação de array e outras operações que exigem um índice

    def __lshift__(self, other):
        """Lida com deslocamento para a esquerda: self << other."""
        if isinstance(other, MutInt):
            return MutInt(self.value << other.value)
        elif isinstance(other, int):
            return MutInt(self.value << other)
        else:
            return NotImplemented

    def __rlshift__(self, other):
        """Lida com deslocamento para a esquerda invertido: other << self."""
        if isinstance(other, int):
            return MutInt(other << self.value)
        else:
            return NotImplemented
```

Adicionamos três novos métodos à classe `MutInt`:

1. `__int__()`: Este método é chamado quando você usa a função `int()` em um objeto da nossa classe `MutInt`. Por exemplo, se você tiver um objeto `MutInt` `a` e escrever `int(a)`, o Python chamará o método `__int__()` do objeto `a`.
2. `__float__()`: Semelhantemente, este método é chamado quando você usa a função `float()` em nosso objeto `MutInt`.
3. `__index__()`: Este método é usado para operações que exigem especificamente um índice inteiro. Por exemplo, quando você deseja acessar um elemento em uma lista usando um índice ou realizar operações de bit, o Python precisa de um índice inteiro.
4. `__lshift__()`: Este método lida com operações de deslocamento para a esquerda quando o objeto `MutInt` está no lado esquerdo do operador `<<`.
5. `__rlshift__()`: Este método lida com operações de deslocamento para a esquerda quando o objeto `MutInt` está no lado direito do operador `<<`.

O método `__index__` é crucial para operações que exigem um índice inteiro, como indexação de lista, fatiamento e operações de bit. Em nossa implementação simples, definimos que ele seja o mesmo que `__int__` porque o valor do nosso objeto `MutInt` pode ser usado diretamente como um índice inteiro.

Os métodos `__lshift__` e `__rlshift__` são essenciais para suportar operações de deslocamento para a esquerda bit a bit. Eles permitem que nossos objetos `MutInt` participem de operações bit a bit, o que é um requisito comum para tipos semelhantes a inteiros.

2. Crie um novo arquivo de teste chamado `test_conversions.py` para testar esses novos métodos:

```python
# test_conversions.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test conversions
print(f"int(a): {int(a)}")
print(f"float(a): {float(a)}")

# Test using as an index
names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
print(f"names[a]: {names[a]}")

# Test using in bit operations (requires __index__)
print(f"1 << a: {1 << a}")  # Shift left by 3

# Test hex/oct/bin functions (requires __index__)
print(f"hex(a): {hex(a)}")
print(f"oct(a): {oct(a)}")
print(f"bin(a): {bin(a)}")

# Modify and test again
a.value = 4
print(f"\nAfter changing value to 4:")
print(f"int(a): {int(a)}")
print(f"names[a]: {names[a]}")
```

3. Execute o script de teste:

```bash
python3 /home/labex/project/test_conversions.py
```

Você deve ver uma saída semelhante a esta:

```
int(a): 3
float(a): 3.0
names[a]: Thomas
1 << a: 8
hex(a): 0x3
oct(a): 0o3
bin(a): 0b11

After changing value to 4:
int(a): 4
names[a]: Lewis
```

Agora nossa classe `MutInt` pode ser convertida para tipos Python padrão e usada em operações que exigem um índice inteiro.

O método `__index__` é particularmente importante. Ele foi introduzido no Python para permitir que objetos fossem usados em situações em que um índice inteiro é necessário, como indexação de lista, operações bit a bit e várias funções como `hex()`, `oct()` e `bin()`.

Com essas adições, nossa classe `MutInt` agora é um tipo primitivo bastante completo. Ele pode ser usado na maioria dos contextos em que um inteiro regular seria usado, com a vantagem adicional de ser mutável.

## Implementação Completa do MutInt

Aqui está nossa implementação completa do `MutInt` com todos os recursos que adicionamos:

```python
# mutint.py

from functools import total_ordering

@total_ordering
class MutInt:
    """
    Uma classe de inteiro mutável que permite que seu valor seja modificado após a criação.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Inicializa com um valor inteiro."""
        self.value = value

    def __str__(self):
        """Retorna uma representação de string para impressão."""
        return str(self.value)

    def __repr__(self):
        """Retorna uma representação de string amigável para desenvolvedores."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Suporta formatação de string com especificações de formato."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Lida com a adição: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Lida com a adição invertida: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Lida com a adição in-place: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Lida com a comparação de igualdade: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Lida com a comparação menor que: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Converte para int."""
        return self.value

    def __float__(self):
        """Converte para float."""
        return float(self.value)

    __index__ = __int__  # Suporta indexação de array e outras operações que exigem um índice

    def __lshift__(self, other):
        """Lida com deslocamento para a esquerda: self << other."""
        if isinstance(other, MutInt):
            return MutInt(self.value << other.value)
        elif isinstance(other, int):
            return MutInt(self.value << other)
        else:
            return NotImplemented

    def __rlshift__(self, other):
        """Lida com deslocamento para a esquerda invertido: other << self."""
        if isinstance(other, int):
            return MutInt(other << self.value)
        else:
            return NotImplemented
```

Esta implementação cobre os principais aspectos da criação de um novo tipo primitivo em Python. Para torná-lo ainda mais completo, você pode implementar métodos adicionais para outras operações como subtração, multiplicação, divisão, etc.
