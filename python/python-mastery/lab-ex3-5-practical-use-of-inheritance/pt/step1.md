# Compreendendo o Problema

Neste laboratório, vamos aprender sobre herança em Python e como ela pode nos ajudar a criar código que seja tanto extensível quanto adaptável. Herança é um conceito poderoso em programação orientada a objetos, onde uma classe pode herdar atributos e métodos de outra classe. Isso nos permite reutilizar código e construir funcionalidades mais complexas com base no código existente.

Vamos começar analisando a função `print_table()` existente. Esta função é o que vamos aprimorar para torná-la mais flexível em termos de formatos de saída.

Primeiro, você precisa abrir o arquivo `tableformat.py` no editor WebIDE. O caminho para este arquivo é o seguinte:

```
/home/labex/project/tableformat.py
```

Depois de abrir o arquivo, você verá a implementação atual da função `print_table()`. Esta função foi projetada para formatar e imprimir dados tabulares. Ela recebe duas entradas principais: uma lista de registros (que são objetos) e uma lista de nomes de campos. Com base nessas entradas, ela imprime uma tabela formatada de forma agradável.

Agora, vamos testar esta função para ver como ela funciona. Abra um terminal no WebIDE e execute os seguintes comandos Python. Esses comandos importam os módulos necessários, leem dados de um arquivo CSV e, em seguida, usam a função `print_table()` para exibir os dados.

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
tableformat.print_table(portfolio, ['name', 'shares', 'price'])
```

Após executar esses comandos, você deve ver a seguinte saída:

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

A saída parece boa, mas há uma limitação nesta função. Atualmente, ela suporta apenas um formato de saída, que é texto simples. Em cenários do mundo real, você pode querer gerar seus dados em diferentes formatos, como CSV, HTML ou outros.

Em vez de fazer alterações na função `print_table()` toda vez que quisermos suportar um novo formato de saída, podemos usar herança para criar uma solução mais flexível. Veja como faremos isso:

1.  Definiremos uma classe base `TableFormatter`. Esta classe terá métodos que são usados para formatar dados. A classe base fornece uma estrutura e funcionalidade comuns sobre as quais todas as subclasses podem ser construídas.
2.  Criaremos várias subclasses. Cada subclasse será projetada para um formato de saída diferente. Por exemplo, uma subclasse pode ser para saída CSV, outra para saída HTML e assim por diante. Essas subclasses herdarão os métodos da classe base e também poderão adicionar sua própria funcionalidade específica.
3.  Modificaremos a função `print_table()` para que ela possa trabalhar com qualquer formatador. Isso significa que podemos passar diferentes subclasses da classe `TableFormatter` para a função `print_table()`, e ela poderá usar os métodos de formatação apropriados.

Essa abordagem tem uma grande vantagem. Ela nos permite adicionar novos formatos de saída sem alterar a funcionalidade principal da função `print_table()`. Portanto, à medida que seus requisitos mudam e você precisa suportar mais formatos de saída, você pode fazê-lo facilmente criando novas subclasses.
