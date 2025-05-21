# Variáveis de Classe e Herança

Neste passo, vamos explorar como as variáveis de classe interagem com a herança e como elas podem servir como um mecanismo de personalização. Em Python, a herança permite que uma subclasse herde atributos e métodos de uma classe base. Variáveis de classe são variáveis que pertencem à própria classe, não a nenhuma instância específica da classe. Compreender como elas funcionam juntas é crucial para criar um código flexível e sustentável.

## Variáveis de Classe na Herança

Quando uma subclasse herda de uma classe base, ela automaticamente obtém acesso às variáveis de classe da classe base. No entanto, uma subclasse tem a capacidade de substituir essas variáveis de classe. Ao fazer isso, a subclasse pode alterar seu comportamento sem afetar a classe base. Este é um recurso muito poderoso, pois permite que você personalize o comportamento de uma subclasse de acordo com suas necessidades específicas.

## Criando uma Classe Stock Especializada

Vamos criar uma subclasse da classe `Stock`. Vamos chamá-la de `DStock`, que significa Decimal Stock. A principal diferença entre `DStock` e a classe `Stock` regular é que `DStock` usará o tipo `Decimal` para valores de preço em vez de `float`. Em cálculos financeiros, a precisão é extremamente importante, e o tipo `Decimal` fornece uma aritmética decimal mais precisa em comparação com `float`.

Para criar esta subclasse, criaremos um novo arquivo chamado `decimal_stock.py`. Aqui está o código que você precisa colocar neste arquivo:

```python
# decimal_stock.py
from decimal import Decimal
from stock import Stock

class DStock(Stock):
    """
    A specialized version of Stock that uses Decimal for prices
    """
    types = (str, int, Decimal)  # Override the types class variable

# Test the subclass
if __name__ == "__main__":
    # Create a DStock from row data
    row = ['AA', '100', '32.20']
    ds = DStock.from_row(row)

    print(f"DStock: {ds.name}")
    print(f"Shares: {ds.shares}")
    print(f"Price: {ds.price} (type: {type(ds.price).__name__})")
    print(f"Cost: {ds.cost()} (type: {type(ds.cost()).__name__})")

    # For comparison, create a regular Stock from the same data
    s = Stock.from_row(row)
    print(f"\nRegular Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price} (type: {type(s.price).__name__})")
    print(f"Cost: {s.cost()} (type: {type(s.cost()).__name__})")
```

Depois de criar o arquivo `decimal_stock.py` com o código acima, você precisa executá-lo para ver os resultados. Abra seu terminal e siga estas etapas:

```bash
cd ~/project
python decimal_stock.py
```

Você deve ver uma saída semelhante a esta:

```
DStock: AA
Shares: 100
Price: 32.20 (type: Decimal)
Cost: 3220.0 (type: Decimal)

Regular Stock: AA
Shares: 100
Price: 32.2 (type: float)
Cost: 3220.0 (type: float)
```

## Pontos-chave sobre Variáveis de Classe e Herança

Deste exemplo, podemos tirar várias conclusões importantes:

1. A classe `DStock` herda todos os métodos da classe `Stock`, como o método `cost()`, sem ter que redefini-los. Esta é uma das principais vantagens da herança, pois evita que você escreva código redundante.
2. Simplesmente substituindo a variável de classe `types`, alteramos como os dados são convertidos ao criar novas instâncias de `DStock`. Isso mostra como as variáveis de classe podem ser usadas para personalizar o comportamento de uma subclasse.
3. A classe base, `Stock`, permanece inalterada e ainda funciona com valores `float`. Isso significa que as alterações que fizemos na subclasse não afetam a classe base, o que é um bom princípio de design.
4. O método de classe `from_row()` funciona corretamente com as classes `Stock` e `DStock`. Isso demonstra o poder da herança, pois o mesmo método pode ser usado com diferentes subclasses.

Este exemplo mostra claramente como as variáveis de classe podem ser usadas como um mecanismo de configuração. As subclasses podem substituir essas variáveis para personalizar seu comportamento sem ter que reescrever os métodos.

## Discussão de Design

Vamos considerar uma abordagem alternativa em que colocamos as conversões de tipo no método `__init__`:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

Com esta abordagem, podemos criar um objeto `Stock` a partir de uma linha de dados assim:

```python
row = ['AA', '100', '32.20']
s = Stock(*row)
```

Embora esta abordagem possa parecer mais simples à primeira vista, ela tem várias desvantagens:

1. Ela combina duas preocupações diferentes: inicialização de objeto e conversão de dados. Isso torna o código mais difícil de entender e manter.
2. O método `__init__` torna-se menos flexível porque sempre converte as entradas, mesmo que já estejam no tipo correto.
3. Restringe como as subclasses podem personalizar o processo de conversão. As subclasses teriam mais dificuldade em alterar a lógica de conversão se ela estivesse incorporada no método `__init__`.
4. O código torna-se mais frágil. Se alguma das conversões falhar, o objeto não poderá ser criado, o que pode levar a erros em seu programa.

Por outro lado, a abordagem do método de classe separa essas preocupações. Isso torna o código mais sustentável e flexível, pois cada parte do código tem uma única responsabilidade.
