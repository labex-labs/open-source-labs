# Tornando Objetos Comparáveis com `__eq__`

Em Python, quando você usa o operador `==` para comparar dois objetos, o Python na verdade chama o método especial `__eq__`. Por padrão, este método compara as identidades dos objetos, o que significa que ele verifica se eles estão armazenados no mesmo endereço de memória, em vez de comparar seus conteúdos.

Vamos dar uma olhada em um exemplo. Suponha que tenhamos uma classe `Stock` e criemos dois objetos `Stock` com os mesmos valores. Então, tentamos compará-los usando o operador `==`. Veja como você pode fazer isso no interpretador Python:

Primeiro, inicie o interpretador Python executando o seguinte comando em seu terminal:

```bash
python3
```

Em seguida, no interpretador Python, execute o seguinte código:

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
False
```

Como você pode ver, embora os dois objetos `Stock` `a` e `b` tenham os mesmos valores para seus atributos (`name`, `shares` e `price`), o Python os considera objetos diferentes porque eles estão armazenados em locais de memória diferentes.

Para corrigir esse problema, podemos implementar o método `__eq__` em nossa classe `Stock`. Este método será chamado toda vez que o operador `==` for usado em objetos da classe `Stock`.

Agora, abra o arquivo `stock.py` novamente. Dentro da classe `Stock`, adicione o seguinte método `__eq__`:

```python
def __eq__(self, other):
    return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                         (other.name, other.shares, other.price))
```

Vamos detalhar o que este método faz:

1. Primeiro, ele usa a função `isinstance` para verificar se o objeto `other` é uma instância da classe `Stock`. Isso é importante porque só queremos comparar objetos `Stock` com outros objetos `Stock`.
2. Se `other` for um objeto `Stock`, ele então compara os atributos (`name`, `shares` e `price`) tanto do objeto `self` quanto do objeto `other`.
3. Ele retorna `True` somente se ambos os objetos forem instâncias `Stock` e seus atributos forem idênticos.

Depois de adicionar o método `__eq__`, sua classe `Stock` completa deve se parecer com isto:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
```

Agora, vamos testar nossa classe `Stock` aprimorada. Inicie o interpretador Python novamente:

```bash
python3
```

Em seguida, execute o seguinte código no interpretador Python:

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
True
>>> c = stock.Stock('GOOG', 200, 490.1)
>>> a == c
False
```

Ótimo! Agora nossos objetos `Stock` podem ser comparados corretamente com base em seu conteúdo, em vez de seus endereços de memória.

A verificação `isinstance` no método `__eq__` é crucial. Ela garante que estamos apenas comparando objetos `Stock`. Se não tivéssemos essa verificação, comparar um objeto `Stock` com algo que não é um objeto `Stock` poderia gerar erros.

Quando terminar de testar, você pode sair do interpretador Python executando o seguinte comando:

```python
>>> exit()
```
