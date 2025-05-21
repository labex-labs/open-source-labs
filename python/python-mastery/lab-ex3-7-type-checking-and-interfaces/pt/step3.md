# Criando Classes de Modelo de Algoritmo

Nesta etapa, vamos usar classes base abstratas para implementar um padrão de método de modelo (template method pattern). O objetivo é reduzir a duplicação de código na funcionalidade de análise de CSV. A duplicação de código pode tornar seu código mais difícil de manter e atualizar. Ao usar o padrão de método de modelo, podemos criar uma estrutura comum para nosso código de análise de CSV e deixar que as subclasses lidem com os detalhes específicos.

## Compreendendo o Padrão de Método de Modelo

O padrão de método de modelo é um padrão de design comportamental. É como um projeto para um algoritmo. Em um método, ele define a estrutura geral ou o "esqueleto" de um algoritmo. No entanto, ele não implementa totalmente todas as etapas. Em vez disso, ele adia algumas das etapas para as subclasses. Isso significa que as subclasses podem redefinir certas partes do algoritmo sem alterar sua estrutura geral.

Em nosso caso, se você olhar o arquivo `reader.py`, notará que as funções `read_csv_as_dicts()` e `read_csv_as_instances()` têm muito código semelhante. A principal diferença entre elas é como elas criam registros a partir das linhas no arquivo CSV. Ao usar o padrão de método de modelo, podemos evitar escrever o mesmo código várias vezes.

## Adicionando a Classe Base CSVParser

Vamos começar adicionando uma classe base abstrata para nossa análise de CSV. Abra o arquivo `reader.py`. Adicionaremos a classe base abstrata `CSVParser` logo no início do arquivo, logo após as instruções de importação.

```python
# reader.py
import csv
from abc import ABC, abstractmethod

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass
```

Esta classe `CSVParser` serve como um modelo para a análise de CSV. O método `parse` contém as etapas comuns para ler um arquivo CSV, como abrir o arquivo, obter os cabeçalhos e iterar sobre as linhas. A lógica específica para criar um registro a partir de uma linha é abstraída no método `make_record()`. Como é um método abstrato, qualquer classe que herde de `CSVParser` deve implementar este método.

## Implementando as Classes Parser Concretas

Agora que temos nossa classe base, precisamos criar as classes parser concretas. Essas classes implementarão a lógica específica de criação de registros.

```python
class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)
```

A classe `DictCSVParser` é usada para criar registros como dicionários. Ela recebe uma lista de tipos em seu construtor. O método `make_record` usa esses tipos para converter os valores na linha e criar um dicionário.

A classe `InstanceCSVParser` é usada para criar registros como instâncias de uma classe. Ela recebe uma classe em seu construtor. O método `make_record` chama o método `from_row` dessa classe para criar uma instância a partir da linha.

## Refatorando as Funções Originais

Agora, vamos refatorar as funções originais `read_csv_as_dicts()` e `read_csv_as_instances()` para usar essas novas classes.

```python
def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dictionaries with appropriate type conversion.
    '''
    parser = DictCSVParser(types)
    return parser.parse(filename)

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of a class.
    '''
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)
```

Essas funções refatoradas têm a mesma interface que as originais. Mas internamente, elas usam as novas classes parser que acabamos de criar. Dessa forma, separamos a lógica comum de análise de CSV da lógica específica de criação de registros.

## Testando sua Implementação

Vamos verificar se nosso código refatorado funciona corretamente. Crie um arquivo chamado `test_reader.py` e adicione o seguinte código a ele.

```python
import reader
import stock

# Test the refactored read_csv_as_instances function
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("First stock:", portfolio[0])

# Test the refactored read_csv_as_dicts function
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First stock as dict:", portfolio_dicts[0])

# Test direct use of a parser
parser = reader.DictCSVParser([str, int, float])
portfolio_dicts2 = parser.parse('portfolio.csv')
print("First stock from direct parser:", portfolio_dicts2[0])
```

Para executar o teste, abra seu terminal e execute o seguinte comando:

```bash
python test_reader.py
```

Você deve ver uma saída semelhante a esta:

```
First stock: Stock('AA', 100, 32.2)
First stock as dict: {'name': 'AA', 'shares': 100, 'price': 32.2}
First stock from direct parser: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

Se você vir esta saída, significa que seu código refatorado está funcionando corretamente. Tanto as funções originais quanto o uso direto de parsers estão produzindo os resultados esperados.
