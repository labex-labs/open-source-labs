# Implementando um Formatador Concreto

Agora que definimos nossa classe base abstrata e atualizamos a função `print_table()`, é hora de criar uma classe formatadora concreta. Uma classe formatadora concreta é aquela que fornece implementações reais para os métodos definidos na classe base abstrata. Em nosso caso, criaremos uma classe que pode formatar dados em uma tabela de texto simples.

Vamos adicionar a seguinte classe ao seu arquivo `tableformat.py`. Esta classe herdará da classe base abstrata `TableFormatter` e implementará os métodos `headings()` e `row()`.

```python
class TextTableFormatter(TableFormatter):
    """
    Formatter that generates a plain - text table.
    """
    def headings(self, headers):
        """
        Generate plain - text table headings.
        """
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        """
        Generate a plain - text table row.
        """
        print(' '.join('%10s' % d for d in rowdata))
```

A classe `TextTableFormatter` herda de `TableFormatter`. Isso significa que ela obtém todas as propriedades e métodos da classe `TableFormatter`, mas também fornece suas próprias implementações para os métodos `headings()` e `row()`. Esses métodos são responsáveis por formatar os cabeçalhos e linhas da tabela, respectivamente. O método `headings()` imprime os cabeçalhos de uma maneira bem formatada, seguido por uma linha de traços para separar os cabeçalhos dos dados. O método `row()` formata cada linha de dados de maneira semelhante.

Agora, vamos testar nosso novo formatador. Usaremos os módulos `stock`, `reader` e `tableformat` para ler dados de um arquivo CSV e imprimi-los usando nosso novo formatador.

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TextTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Quando você executar este código, você deve ver a mesma saída de antes. Isso ocorre porque nosso novo formatador foi projetado para produzir a mesma tabela de texto simples que a função `print_table()` original.

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Esta saída confirma que nosso `TextTableFormatter` está funcionando corretamente. A vantagem de usar essa abordagem é que tornamos nosso código mais modular e extensível. Ao separar a lógica de formatação em uma hierarquia de classes separada, podemos facilmente adicionar novos formatos de saída. Tudo o que precisamos fazer é criar novas subclasses de `TableFormatter` sem modificar a função `print_table()`. Dessa forma, podemos suportar diferentes formatos de saída, como CSV ou HTML, no futuro.
