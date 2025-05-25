# Exercício 3.2: Criando uma função de nível superior para a execução do programa

Pegue a última parte do seu programa e empacote-a em uma única função `portfolio_report(portfolio_filename, prices_filename)`. Faça com que a função funcione de modo que a seguinte chamada de função crie o relatório como antes:

```python
portfolio_report('/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv')
```

Nesta versão final, seu programa não será nada mais do que uma série de definições de função, seguida por uma única chamada de função para `portfolio_report()` no final (que executa todas as etapas envolvidas no programa).

Ao transformar seu programa em uma única função, torna-se fácil executá-lo com diferentes entradas. Por exemplo, experimente estas instruções interativamente após executar seu programa:

```python
>>> portfolio_report('/home/labex/project/portfolio2.csv', '/home/labex/project/prices.csv')
... veja a saída ...
>>> files = ['/home/labex/project/portfolio.csv', '/home/labex/project/portfolio2.csv']
>>> for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, '/home/labex/project/prices.csv')
        print()

... veja a saída ...
>>>
```
