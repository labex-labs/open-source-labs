# Melhorando a Representação de String

Quando você imprime um objeto `MutInt` em Python, você verá uma saída como `<__main__.MutInt object at 0x...>`. Essa saída não é muito útil porque não informa o valor real do objeto `MutInt`. Para facilitar a compreensão do que o objeto representa, vamos implementar métodos especiais para representação de string.

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
```

Adicionamos três métodos importantes à classe `MutInt`:

- `__str__()`: Este método é chamado quando você usa a função `str()` no objeto ou quando você imprime o objeto diretamente. Ele deve retornar uma string legível por humanos.
- `__repr__()`: Este método fornece a representação de string "oficial" do objeto. Ele é usado principalmente para depuração e, idealmente, deve retornar uma string que, se passada para a função `eval()`, recriaria o objeto.
- `__format__()`: Este método permite que você use o sistema de formatação de string do Python com seus objetos `MutInt`. Você pode usar especificações de formato como preenchimento e formatação de números.

2. Crie um novo arquivo de teste chamado `test_string_repr.py` para testar esses novos métodos:

```python
# test_string_repr.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test string representation
print(f"str(a): {str(a)}")
print(f"repr(a): {repr(a)}")

# Test direct printing
print(f"Print a: {a}")

# Test string formatting
print(f"Formatted with padding: '{a:*^10}'")
print(f"Formatted as decimal: '{a:d}'")

# Test mutability
a.value = 42
print(f"After changing value, repr(a): {repr(a)}")
```

Neste arquivo de teste, primeiro importamos a classe `MutInt`. Em seguida, criamos um objeto `MutInt` com o valor `3`. Testamos os métodos `__str__()` e `__repr__()` usando as funções `str()` e `repr()`. Também testamos a impressão direta, a formatação de string e a mutabilidade do objeto `MutInt`.

3. Execute o script de teste:

```bash
python3 /home/labex/project/test_string_repr.py
```

Quando você executa este comando, o Python executará o script `test_string_repr.py`. Você deve ver uma saída semelhante a esta:

```
str(a): 3
repr(a): MutInt(3)
Print a: 3
Formatted with padding: '****3*****'
Formatted as decimal: '3'
After changing value, repr(a): MutInt(42)
```

Agora nossos objetos `MutInt` são exibidos de forma agradável. A representação de string mostra o valor subjacente, e podemos usar a formatação de string como com inteiros regulares.

A diferença entre `__str__()` e `__repr__()` é que `__str__()` é projetado para produzir uma saída amigável para humanos, enquanto `__repr__()` idealmente deve produzir uma string que, quando passada para `eval()`, recriaria o objeto. É por isso que incluímos o nome da classe no método `__repr__()`.

O método `__format__()` permite que nosso objeto trabalhe com o sistema de formatação do Python, para que possamos usar especificações de formato como preenchimento e formatação de números.
