# Exercício 9.2: Criando um diretório de aplicação

Colocar todo o seu código em um "pacote" (package) geralmente não é suficiente para uma aplicação. Às vezes, existem arquivos de suporte, documentação, scripts e outras coisas. Esses arquivos precisam existir FORA do diretório `porty/` que você criou acima.

Crie um novo diretório chamado `porty-app`. Mova o diretório `porty` que você criou no Exercício 9.1 para dentro desse diretório. Copie os arquivos de teste `portfolio.csv` e `prices.csv` para este diretório. Adicionalmente, crie um arquivo `README.txt` com algumas informações sobre você. Seu código agora deve ser organizado da seguinte forma:

    porty-app/
        portfolio.csv
        prices.csv
        README.txt
        porty/
            __init__.py
            fileparse.py
            follow.py
            pcost.py
            portfolio.py
            report.py
            stock.py
            tableformat.py
            ticker.py
            typedproperty.py

Para executar seu código, você precisa ter certeza de que está trabalhando no diretório de nível superior `porty-app/`. Por exemplo, no terminal:

```python
$ cd porty-app
$ python3
>>> import porty.report
>>>
```

Tente executar alguns de seus scripts anteriores como um programa principal:

```python
$ cd porty-app
$ python3 -m porty.report portfolio.csv prices.csv txt
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84

$
```
