# Adicionando Operações Matemáticas

Atualmente, nossa classe `MutInt` não suporta operações matemáticas como adição. Em Python, para habilitar tais operações para uma classe personalizada, precisamos implementar métodos especiais. Esses métodos especiais também são conhecidos como "métodos mágicos" ou "métodos dunder" porque são cercados por sublinhados duplos. Vamos adicionar a funcionalidade de adição implementando os métodos especiais relevantes para operações aritméticas.

1. Abra `mutint.py` no WebIDE e atualize-o com o seguinte código:

```python
# mutint.py

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
        # For commutative operations like +, we can reuse __add__
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
```

Adicionamos três novos métodos à classe `MutInt`:

- `__add__()`: Este método é chamado quando o operador `+` é usado com nosso objeto `MutInt` no lado esquerdo. Dentro deste método, primeiro verificamos se o operando `other` é uma instância de `MutInt` ou um `int`. Se for, realizamos a adição e retornamos um novo objeto `MutInt` com o resultado. Se o operando `other` for outra coisa, retornamos `NotImplemented`. Isso diz ao Python para tentar outros métodos ou lançar um `TypeError`.
- `__radd__()`: Este método é chamado quando o operador `+` é usado com nosso objeto `MutInt` no lado direito. Como a adição é uma operação comutativa (ou seja, `a + b` é o mesmo que `b + a`), podemos simplesmente reutilizar o método `__add__`.
- `__iadd__()`: Este método é chamado quando o operador `+=` é usado em nosso objeto `MutInt`. Em vez de criar um novo objeto, ele modifica o objeto `MutInt` existente e o retorna.

2. Crie um novo arquivo de teste chamado `test_math_ops.py` para testar esses novos métodos:

```python
# test_math_ops.py

from mutint import MutInt

# Create MutInt objects
a = MutInt(3)
b = MutInt(5)

# Test regular addition
c = a + b
print(f"a + b = {c}")

# Test addition with int
d = a + 10
print(f"a + 10 = {d}")

# Test reversed addition
e = 7 + a
print(f"7 + a = {e}")

# Test in-place addition
print(f"Before a += 5: a = {a}")
a += 5
print(f"After a += 5: a = {a}")

# Test in-place addition with reference sharing
f = a  # f and a point to the same object
print(f"Before a += 10: a = {a}, f = {f}")
a += 10
print(f"After a += 10: a = {a}, f = {f}")

# Test unsupported operation
try:
    result = a + 3.5  # Adding a float is not supported
    print(f"a + 3.5 = {result}")
except TypeError as e:
    print(f"Error when adding float: {e}")
```

Neste arquivo de teste, primeiro importamos a classe `MutInt`. Em seguida, criamos alguns objetos `MutInt` e realizamos diferentes tipos de operações de adição. Também testamos a adição in-place e o caso em que uma operação não suportada (adicionando um float) é tentada.

3. Execute o script de teste:

```bash
python3 /home/labex/project/test_math_ops.py
```

Você deve ver uma saída semelhante a esta:

```
a + b = MutInt(8)
a + 10 = MutInt(13)
7 + a = MutInt(10)
Before a += 5: a = MutInt(3)
After a += 5: a = MutInt(8)
Before a += 10: a = MutInt(8), f = MutInt(8)
After a += 10: a = MutInt(18), f = MutInt(18)
Error when adding float: unsupported operand type(s) for +: 'MutInt' and 'float'
```

Agora nossa classe `MutInt` suporta operações básicas de adição. Observe que quando usamos `+=`, tanto `a` quanto `f` foram atualizados. Isso mostra que `a += 10` modificou o objeto existente em vez de criar um novo.

Este comportamento com objetos mutáveis é semelhante aos tipos mutáveis embutidos do Python, como listas. Por exemplo:

```python
a = [1, 2, 3]
b = a
a += [4, 5]  # Both a and b are updated
```

Em contraste, para tipos imutáveis como tuplas, `+=` cria um novo objeto:

```python
c = (1, 2, 3)
d = c
c += (4, 5)  # c is a new object, d still points to the old one
```
