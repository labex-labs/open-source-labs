# Exercício 2.9: Coletando Dados

No Exercício 2.7, você escreveu um programa chamado `report.py` que calculava o ganho/perda de uma carteira de ações. Neste exercício, você começará a modificá-lo para produzir uma tabela como esta:

          Name     Shares      Price     Change
    ---------- ---------- ---------- ----------
            AA        100       9.22     -22.98
           IBM         50     106.28      15.18
           CAT        150      35.46     -47.98
          MSFT        200      20.89     -30.34
            GE         95      13.48     -26.89
          MSFT         50      20.89     -44.21
           IBM        100     106.28      35.84

Neste relatório, "Price" (Preço) é o preço atual da ação e "Change" (Mudança) é a mudança no preço da ação em relação ao preço de compra inicial.

Para gerar o relatório acima, você primeiro precisará coletar todos os dados mostrados na tabela. Escreva uma função `make_report()` que recebe uma lista de ações e um dicionário de preços como entrada e retorna uma lista de tuplas contendo as linhas da tabela acima.

Adicione esta função ao seu arquivo `report.py`. Veja como ela deve funcionar se você tentar interativamente:

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> prices = read_prices('/home/labex/project/prices.csv')
>>> report = make_report(portfolio, prices)
>>> for r in report:
        print(r)

('AA', 100, 9.22, -22.980000000000004)
('IBM', 50, 106.28, 15.180000000000007)
('CAT', 150, 35.46, -47.98)
('MSFT', 200, 20.89, -30.339999999999996)
('GE', 95, 13.48, -26.889999999999997)
...
>>>
```
