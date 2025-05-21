# Criando um Leitor CSV de Propósito Geral

Neste passo final, vamos criar uma função de propósito geral. Esta função será capaz de ler arquivos CSV e criar objetos de qualquer classe que tenha implementado o método de classe `from_row()`. Isso nos mostra o poder de usar métodos de classe como uma interface uniforme. Uma interface uniforme significa que diferentes classes podem ser usadas da mesma maneira, o que torna nosso código mais flexível e fácil de gerenciar.

## Modificando a Função read_portfolio()

Primeiro, atualizaremos a função `read_portfolio()` no arquivo `stock.py`. Usaremos nosso novo método de classe `from_row()`. Abra o arquivo `stock.py` e altere a função `read_portfolio()` assim:

```python
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of Stock instances
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            portfolio.append(Stock.from_row(row))
    return portfolio
```

Esta nova versão da função é mais simples. Ela dá a responsabilidade da conversão de tipo à classe `Stock`, onde ela realmente pertence. Conversão de tipo significa mudar os dados de um tipo para outro, como transformar uma string em um inteiro. Ao fazer isso, tornamos nosso código mais organizado e fácil de entender.

## Criando um Leitor CSV de Propósito Geral

Agora, criaremos uma função de propósito mais geral no arquivo `reader.py`. Esta função pode ler dados CSV e criar instâncias de qualquer classe que tenha um método de classe `from_row()`.

Abra o arquivo `reader.py` e adicione a seguinte função:

```python
def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of the given class.

    Args:
        filename: Name of the CSV file
        cls: Class to instantiate (must have from_row class method)

    Returns:
        List of class instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

Esta função recebe duas entradas: um nome de arquivo e uma classe. Em seguida, retorna uma lista de instâncias dessa classe, criadas a partir dos dados no arquivo CSV. Isso é muito útil porque podemos usá-lo com diferentes classes, desde que elas tenham o método `from_row()`.

## Testando o Leitor CSV de Propósito Geral

Vamos criar um arquivo de teste para ver como nosso leitor de propósito geral funciona. Crie um arquivo chamado `test_csv_reader.py` com o seguinte conteúdo:

```python
# test_csv_reader.py
from reader import read_csv_as_instances
from stock import Stock
from decimal_stock import DStock

# Read portfolio as Stock instances
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print(f"Portfolio contains {len(portfolio)} stocks")
print(f"First stock: {portfolio[0].name}, {portfolio[0].shares} shares at ${portfolio[0].price}")

# Read portfolio as DStock instances (with Decimal prices)
decimal_portfolio = read_csv_as_instances('portfolio.csv', DStock)
print(f"\nDecimal portfolio contains {len(decimal_portfolio)} stocks")
print(f"First stock: {decimal_portfolio[0].name}, {decimal_portfolio[0].shares} shares at ${decimal_portfolio[0].price}")

# Define a new class for reading the bus data
class BusRide:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

    @classmethod
    def from_row(cls, row):
        return cls(row[0], row[1], row[2], int(row[3]))

# Read some bus data (just the first 5 records for brevity)
print("\nReading bus data...")
import csv
with open('ctabus.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Skip header
    bus_rides = []
    for i, row in enumerate(rows):
        if i >= 5:  # Only read 5 records for the example
            break
        bus_rides.append(BusRide.from_row(row))

# Display the bus data
for ride in bus_rides:
    print(f"Route: {ride.route}, Date: {ride.date}, Type: {ride.daytype}, Rides: {ride.rides}")
```

Execute este arquivo para ver os resultados. Abra seu terminal e use os seguintes comandos:

```bash
cd ~/project
python test_csv_reader.py
```

Você deve ver uma saída que mostra os dados do portfólio carregados como instâncias `Stock` e `DStock`, e os dados da rota do ônibus carregados como instâncias `BusRide`. Isso prova que nosso leitor de propósito geral funciona com diferentes classes.

## Principais Benefícios desta Abordagem

Esta abordagem mostra vários conceitos poderosos:

1. **Separação de preocupações**: Ler dados é separado da criação de objetos. Isso significa que o código para ler o arquivo CSV não é misturado com o código para criar objetos. Isso torna o código mais fácil de entender e manter.
2. **Polimorfismo**: O mesmo código pode funcionar com diferentes classes que seguem a mesma interface. Em nosso caso, desde que uma classe tenha o método `from_row()`, nosso leitor de propósito geral pode usá-lo.
3. **Flexibilidade**: Podemos facilmente alterar como os dados são convertidos usando classes diferentes. Por exemplo, podemos usar `Stock` ou `DStock` para lidar com os dados do portfólio de maneira diferente.
4. **Extensibilidade**: Podemos adicionar novas classes que funcionam com nosso leitor sem alterar o código do leitor. Isso torna nosso código mais preparado para o futuro.

Este é um padrão comum em Python que torna o código mais modular, reutilizável e sustentável.

## Notas Finais sobre Métodos de Classe

Métodos de classe são frequentemente usados como construtores alternativos em Python. Você geralmente pode diferenciá-los porque seus nomes geralmente têm a palavra "from" neles. Por exemplo:

```python
# Some examples from Python's built-in types
dict.fromkeys(['a', 'b', 'c'], 0)  # Create a dict with default values
datetime.datetime.fromtimestamp(1627776000)  # Create datetime from timestamp
int.from_bytes(b'\x00\x01', byteorder='big')  # Create int from bytes
```

Ao seguir esta convenção, você torna seu código mais legível e consistente com as bibliotecas integradas do Python. Isso ajuda outros desenvolvedores a entender seu código mais facilmente.
