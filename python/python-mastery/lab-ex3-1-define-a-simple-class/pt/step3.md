# Formatação e Impressão dos Dados da Carteira

Nesta etapa, vamos criar uma função que nos ajudará a exibir os dados da carteira em uma tabela bem organizada. Uma carteira é uma coleção de ações, e é importante apresentar esses dados de forma clara e legível. É aí que a função `print_portfolio(portfolio)` entra em ação. Esta função receberá uma carteira como entrada e a exibirá em uma tabela com cabeçalhos e alinhamento adequado.

## Formatação de Strings em Python

Em Python, existem várias maneiras de formatar strings. A formatação de strings é uma habilidade crucial, pois permite que você apresente dados de maneira mais organizada e amigável ao usuário.

- O operador `%` é um estilo mais antigo de formatação de strings. É como um modelo onde você pode inserir valores em locais específicos em uma string.
- O método `str.format()` é outra maneira. Ele oferece mais flexibilidade e uma sintaxe mais limpa para formatar strings.
- f-strings são um recurso introduzido no Python 3.6 e posterior. Eles são muito convenientes, pois permitem que você incorpore expressões dentro de literais de string.

Para este exercício, usaremos o operador `%`. Ele é particularmente útil quando você deseja criar colunas de largura fixa, que é exatamente o que precisamos para nossa tabela de carteira.

## Instruções de Implementação

1. Primeiro, abra o arquivo `stock.py` no seu editor. Se já estiver aberto, ótimo. Este arquivo é onde escreveremos nossa função `print_portfolio`.

2. Depois que o arquivo estiver aberto, procure o comentário `# TODO: Add print_portfolio(portfolio) function here`. Este comentário é um marcador que nos diz onde adicionar nossa nova função.

3. Abaixo desse comentário, adicione a seguinte função:

```python
def print_portfolio(portfolio):
    """
    Print the portfolio data in a nicely formatted table.

    Args:
        portfolio (list): A list of Stock objects
    """
    # Print the header row
    print('%10s %10s %10s' % ('name', 'shares', 'price'))

    # Print a separator line
    print('-' * 10 + ' ' + '-' * 10 + ' ' + '-' * 10)

    # Print each stock in the portfolio
    for stock in portfolio:
        print('%10s %10d %10.2f' % (stock.name, stock.shares, stock.price))
```

Esta função primeiro imprime a linha de cabeçalho da tabela, depois uma linha separadora e, finalmente, percorre cada ação na carteira e imprime seus detalhes de forma formatada.

4. Depois de adicionar a função, salve o arquivo. Você pode fazer isso pressionando `Ctrl+S` ou selecionando "File > Save" no menu. Salvar o arquivo garante que suas alterações sejam preservadas.

5. Agora, precisamos testar nossa função. Crie um novo arquivo chamado `test_print.py`. Este arquivo será nosso script de teste. Adicione o seguinte código a ele:

```python
# test_print.py
from stock import read_portfolio, print_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a formatted table
print_portfolio(portfolio)
```

Este script importa as funções `read_portfolio` e `print_portfolio` do arquivo `stock.py`. Em seguida, ele lê os dados da carteira de um arquivo CSV e usa nossa função `print_portfolio` recém-criada para exibi-los.

6. Finalmente, execute o script de teste. Abra seu terminal e digite o seguinte comando:

```bash
python3 test_print.py
```

Se tudo estiver funcionando corretamente, você deverá ver uma saída como esta:

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Esta saída confirma que sua função `print_portfolio` está funcionando conforme o esperado. Ela formata e exibe os dados da carteira em uma tabela com cabeçalhos e colunas alinhadas, tornando-a fácil de ler.

## Entendendo a Formatação de Strings

Vamos analisar mais de perto como a formatação de strings funciona na função `print_portfolio`.

- `%10s` é usado para formatar uma string. O `10` indica a largura do campo, e o `s` significa string. Ele alinha a string à direita dentro de um campo com largura 10.
- `%10d` é para formatar um inteiro. O `10` é a largura do campo, e `d` representa um inteiro. Ele também alinha o inteiro à direita em um campo com largura 10.
- `%10.2f` é usado para formatar um float. O `10` é a largura do campo, e o `.2` especifica que queremos exibir o float com 2 casas decimais. Ele alinha o float à direita em um campo com largura 10.

Essa formatação garante que todas as colunas em nossa tabela sejam devidamente alinhadas, o que torna a saída muito mais fácil de ler e entender.
