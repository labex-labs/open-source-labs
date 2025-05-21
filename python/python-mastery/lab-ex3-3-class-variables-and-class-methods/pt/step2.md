# Implementando Construtores Alternativos com Métodos de Classe

Neste passo, vamos aprender como implementar um construtor alternativo usando um método de classe. Isso nos permitirá criar objetos `Stock` a partir de dados de linha CSV de uma forma mais elegante.

## O que é um Construtor Alternativo?

Em Python, um construtor alternativo é um padrão útil. Normalmente, criamos objetos usando o método padrão `__init__`. No entanto, um construtor alternativo nos dá uma maneira adicional de criar objetos. Métodos de classe são muito adequados para implementar construtores alternativos porque podem acessar a própria classe.

## Implementando o Método de Classe from_row()

Adicionaremos uma variável de classe `types` e um método de classe `from_row()` à nossa classe `Stock`. Isso simplificará o processo de criação de instâncias `Stock` a partir de dados CSV.

Vamos modificar o arquivo `stock.py` adicionando o código destacado:

```python
# stock.py

class Stock:
    types = (str, int, float)  # Type conversions to apply to CSV data

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    @classmethod
    def from_row(cls, row):
        """
        Create a Stock instance from a row of CSV data.

        Args:
            row: A list of strings [name, shares, price]

        Returns:
            A new Stock instance
        """
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

# The rest of the file remains unchanged
```

Agora, vamos entender o que está acontecendo neste código passo a passo:

1. Definimos uma variável de classe `types`. É uma tupla que contém funções de conversão de tipo `(str, int, float)`. Essas funções serão usadas para converter os dados da linha CSV para os tipos apropriados.
2. Adicionamos um método de classe `from_row()`. O decorador `@classmethod` marca este método como um método de classe.
3. O primeiro parâmetro deste método é `cls`, que é uma referência à própria classe. Em métodos normais, usamos `self` para nos referir a uma instância da classe, mas aqui usamos `cls` porque é um método de classe.
4. A função `zip()` é usada para emparelhar cada função de conversão de tipo em `types` com o valor correspondente na lista `row`.
5. Usamos uma compreensão de lista para aplicar cada função de conversão ao valor correspondente na lista `row`. Desta forma, convertemos os dados de string da linha CSV para os tipos apropriados.
6. Finalmente, criamos uma nova instância da classe `Stock` usando os valores convertidos e a retornamos.

## Testando o Construtor Alternativo

Agora, criaremos um novo arquivo chamado `test_class_method.py` para testar nosso novo método de classe. Isso nos ajudará a verificar se o construtor alternativo funciona como esperado.

```python
# test_class_method.py
from stock import Stock

# Test the from_row() class method
row = ['AA', '100', '32.20']
s = Stock.from_row(row)

print(f"Stock: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost()}")

# Try with a different row
row2 = ['GOOG', '50', '1120.50']
s2 = Stock.from_row(row2)

print(f"\nStock: {s2.name}")
print(f"Shares: {s2.shares}")
print(f"Price: {s2.price}")
print(f"Cost: {s2.cost()}")
```

Para ver os resultados, execute os seguintes comandos no seu terminal:

```bash
cd ~/project
python test_class_method.py
```

Você deve ver uma saída semelhante a esta:

```
Stock: AA
Shares: 100
Price: 32.2
Cost: 3220.0

Stock: GOOG
Shares: 50
Price: 1120.5
Cost: 56025.0
```

Observe que agora podemos criar instâncias `Stock` diretamente a partir de dados de string sem ter que realizar manualmente as conversões de tipo fora da classe. Isso torna nosso código mais limpo e garante que a responsabilidade pela conversão de dados seja tratada dentro da própria classe.
