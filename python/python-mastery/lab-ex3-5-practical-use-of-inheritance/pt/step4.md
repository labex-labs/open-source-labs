# Criando Formatadores Adicionais

Em programação, herança é um conceito poderoso que nos permite criar novas classes com base nas existentes. Isso ajuda a reutilizar código e tornar nossos programas mais extensíveis. Nesta parte do experimento, usaremos herança para criar dois novos formatadores para diferentes formatos de saída: CSV e HTML. Esses formatadores herdarão de uma classe base, o que significa que compartilharão algum comportamento comum, enquanto terão suas próprias maneiras únicas de formatar dados.

Agora, vamos adicionar as seguintes classes ao seu arquivo `tableformat.py`. Essas classes definirão como formatar dados nos formatos CSV e HTML, respectivamente.

```python
class CSVTableFormatter(TableFormatter):
    """
    Formatter that generates CSV formatted data.
    """
    def headings(self, headers):
        """
        Generate CSV headers.
        """
        print(','.join(headers))

    def row(self, rowdata):
        """
        Generate a CSV data row.
        """
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    """
    Formatter that generates HTML table code.
    """
    def headings(self, headers):
        """
        Generate HTML table headers.
        """
        print('<tr>', end=' ')
        for header in headers:
            print(f'<th>{header}</th>', end=' ')
        print('</tr>')

    def row(self, rowdata):
        """
        Generate an HTML table row.
        """
        print('<tr>', end=' ')
        for data in rowdata:
            print(f'<td>{data}</td>', end=' ')
        print('</tr>')
```

A classe `CSVTableFormatter` foi projetada para formatar dados no formato CSV (Valores Separados por Vírgula). O método `headings` recebe uma lista de cabeçalhos e os imprime separados por vírgulas. O método `row` recebe uma lista de dados para uma única linha e também os imprime separados por vírgulas.

A classe `HTMLTableFormatter`, por outro lado, é usada para gerar código de tabela HTML. O método `headings` cria os cabeçalhos da tabela usando as tags HTML `<th>`, e o método `row` cria uma linha da tabela usando as tags HTML `<td>`.

Vamos testar esses novos formatadores para ver como eles funcionam.

1. Primeiro, vamos testar o formatador CSV:

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.CSVTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Neste código, primeiro importamos os módulos necessários. Em seguida, lemos dados de um arquivo CSV chamado `portfolio.csv` e criamos instâncias da classe `Stock`. Em seguida, criamos uma instância da classe `CSVTableFormatter`. Finalmente, usamos a função `print_table` para imprimir os dados do portfólio em formato CSV.

Você deve ver a seguinte saída formatada em CSV:

```
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44
```

2. Agora, vamos testar o formatador HTML:

```python
formatter = tableformat.HTMLTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Aqui, criamos uma instância da classe `HTMLTableFormatter` e usamos a função `print_table` novamente para imprimir os dados do portfólio em formato HTML.

Você deve ver a seguinte saída formatada em HTML:

```
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

Como você pode ver, cada formatador produz saída em um formato diferente, mas todos eles compartilham a mesma interface definida pela classe base `TableFormatter`. Este é um ótimo exemplo do poder da herança e do polimorfismo. Podemos escrever código que funciona com a classe base, e ele funcionará automaticamente com qualquer subclasse.

A função `print_table()` não precisa saber nada sobre o formatador específico que está sendo usado. Ela apenas chama os métodos definidos na classe base, e a implementação apropriada é selecionada com base no tipo de formatador fornecido. Isso torna nosso código mais flexível e fácil de manter.
