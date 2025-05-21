# Testando Nossa Implementação

Agora que implementamos nossa metaclasse e modificamos a classe `Structure`, é hora de testar nossa implementação. Testar é crucial porque nos ajuda a garantir que tudo está funcionando corretamente. Ao executar testes, podemos detectar quaisquer problemas potenciais no início e garantir que nosso código se comporte conforme o esperado.

Primeiro, vamos executar os testes unitários para ver se nossa classe `Stock` funciona como esperado. Testes unitários são testes pequenos e isolados que verificam partes individuais do nosso código. Neste caso, queremos ter certeza de que a classe `Stock` funciona corretamente. Para executar os testes unitários, usaremos o seguinte comando no terminal:

```bash
python3 teststock.py
```

Se tudo estiver funcionando corretamente, todos os testes devem passar sem erros. Quando os testes são executados com sucesso, a saída deve ser semelhante a esta:

```
........
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

Os pontos representam cada teste que passou, e o `OK` final indica que todos os testes foram bem-sucedidos.

Agora, vamos testar nossa classe `Stock` com alguns dados reais e a funcionalidade de formatação de tabela. Isso nos dará um cenário mais real para ver como nossa classe `Stock` interage com os dados e como a formatação da tabela funciona. Usaremos o seguinte comando no terminal:

```bash
python3 -c "
from stock import Stock
from reader import read_csv_as_instances
from tableformat import create_formatter, print_table

# Lê os dados do portfólio em instâncias Stock
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print('Portfolio:')
print(portfolio)

# Formata e imprime os dados do portfólio
print('\nTabela formatada:')
formatter = create_formatter('text')
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Neste código, primeiro importamos as classes e funções necessárias. Em seguida, lemos dados de um arquivo CSV em instâncias `Stock`. Depois disso, imprimimos os dados do portfólio e, em seguida, formatamos em uma tabela e imprimimos a tabela formatada.

Você deve ver uma saída semelhante a esta:

```
Portfolio:
[Stock('AA',100,32.2), Stock('IBM',50,91.1), Stock('CAT',150,83.44), Stock('MSFT',200,51.23), Stock('GE',95,40.37), Stock('MSFT',50,65.1), Stock('IBM',100,70.44)]

Formatted table:
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

Reserve um momento para apreciar o que realizamos:

1. Criamos um mecanismo para coletar automaticamente todos os tipos de validadores. Isso significa que não precisamos acompanhar manualmente todos os validadores, o que economiza tempo e reduz a chance de erros.
2. Implementamos uma metaclasse que injeta esses tipos no namespace das subclasses `Structure`. Isso permite que as subclasses usem esses validadores sem ter que importá-los explicitamente.
3. Eliminamos a necessidade de importações explícitas de tipos de validadores. Isso torna nosso código mais limpo e mais fácil de ler.
4. Tudo isso acontece nos bastidores, tornando o código para definir novas estruturas limpo e simples.

O arquivo `stock.py` final é notavelmente limpo em comparação com o que seria sem nossa metaclasse:

```python
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Sem a necessidade de importar os tipos de validadores diretamente, o código é mais conciso e fácil de manter. Este é um ótimo exemplo de como as metaclasses podem melhorar a qualidade do nosso código.
