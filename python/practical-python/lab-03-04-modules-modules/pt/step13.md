# Exercício 3.12: Usando seu módulo de biblioteca

Na seção 2, você escreveu um programa `report.py` que produzia um relatório de ações como este:

          Name     Shares      Price     Change
    ---------- ---------- ---------- ----------
            AA        100       9.22     -22.98
           IBM         50     106.28      15.18
           CAT        150      35.46     -47.98
          MSFT        200      20.89     -30.34
            GE         95      13.48     -26.89
          MSFT         50      20.89     -44.21
           IBM        100     106.28      35.84

Pegue esse programa e modifique-o para que todo o processamento do arquivo de entrada seja feito usando funções em seu módulo `fileparse`. Para fazer isso, importe `fileparse` como um módulo e altere as funções `read_portfolio()` e `read_prices()` para usar a função `parse_csv()`.

Use o exemplo interativo no início deste exercício como guia. Depois, você deve obter exatamente a mesma saída de antes.
