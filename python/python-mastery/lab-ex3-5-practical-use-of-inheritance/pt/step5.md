# Criando uma Função Fábrica

Ao usar herança, um desafio comum é que os usuários precisam se lembrar dos nomes das classes formatadoras específicas. Isso pode ser um incômodo, especialmente à medida que o número de classes aumenta. Para simplificar esse processo, podemos criar uma função fábrica. Uma função fábrica é um tipo especial de função que cria e retorna objetos. Em nosso caso, ela retornará o formatador apropriado com base em um nome de formato simples.

Vamos adicionar a seguinte função ao seu arquivo `tableformat.py`. Esta função receberá um nome de formato como argumento e retornará o objeto formatador correspondente.

```python
def create_formatter(format_name):
    """
    Create a formatter of the specified type.

    Args:
        format_name: Name of the formatter ('text', 'csv', 'html')

    Returns:
        A TableFormatter object

    Raises:
        ValueError: If format_name is not recognized
    """
    if format_name == 'text':
        return TextTableFormatter()
    elif format_name == 'csv':
        return CSVTableFormatter()
    elif format_name == 'html':
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {format_name}')
```

A função `create_formatter()` é uma função fábrica. Ela verifica o argumento `format_name` que você fornece. Se for 'text', ela cria e retorna um objeto `TextTableFormatter`. Se for 'csv', ela retorna um objeto `CSVTableFormatter`, e se for 'html', ela retorna um objeto `HTMLTableFormatter`. Se o nome do formato não for reconhecido, ela levanta um `ValueError`. Dessa forma, os usuários podem selecionar facilmente um formatador apenas fornecendo um nome simples, sem precisar conhecer os nomes específicos das classes.

Agora, vamos testar a função fábrica. Usaremos algumas funções e classes existentes para ler dados de um arquivo CSV e imprimi-los em diferentes formatos.

```python
import stock
import reader
from tableformat import create_formatter, print_table

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Test with text formatter
formatter = create_formatter('text')
print("\nText Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with CSV formatter
formatter = create_formatter('csv')
print("\nCSV Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with HTML formatter
formatter = create_formatter('html')
print("\nHTML Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Neste código, primeiro importamos os módulos e funções necessários. Em seguida, lemos dados do arquivo `portfolio.csv` e criamos um objeto `portfolio`. Depois disso, testamos a função `create_formatter()` com diferentes nomes de formato: 'text', 'csv' e 'html'. Para cada formato, criamos um objeto formatador, imprimimos o nome do formato e, em seguida, usamos a função `print_table()` para imprimir os dados do `portfolio` no formato especificado.

Quando você executar este código, você deverá ver a saída em todos os três formatos, separados pelo nome do formato:

```
Text Format:
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44

CSV Format:
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44

HTML Format:
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

A função fábrica torna o código mais amigável, pois oculta os detalhes da instanciação da classe. Os usuários não precisam saber como criar objetos formatadores; eles só precisam especificar o formato desejado.

Este padrão de usar uma função fábrica para criar objetos é um padrão de projeto comum em programação orientada a objetos, conhecido como Padrão de Fábrica (Factory Pattern). Ele fornece uma camada de abstração entre o código do cliente (o código que usa o formatador) e as classes de implementação reais (as classes formatadoras). Isso torna o código mais modular e fácil de usar.

**Revisão dos Conceitos-Chave:**

1.  **Classe Base Abstrata (Abstract Base Class)**: A classe `TableFormatter` serve como uma interface. Uma interface define um conjunto de métodos que todas as classes que a implementam devem ter. Em nosso caso, todas as classes formatadoras devem implementar os métodos definidos na classe `TableFormatter`.

2.  **Herança (Inheritance)**: As classes formatadoras concretas, como `TextTableFormatter`, `CSVTableFormatter` e `HTMLTableFormatter`, herdam da classe base `TableFormatter`. Isso significa que elas obtêm a estrutura básica e os métodos da classe base e podem fornecer suas próprias implementações específicas.

3.  **Polimorfismo (Polymorphism)**: A função `print_table()` pode trabalhar com qualquer formatador que implemente a interface necessária. Isso significa que você pode passar diferentes objetos formatadores para a função `print_table()`, e ela funcionará corretamente com cada um.

4.  **Padrão de Fábrica (Factory Pattern)**: A função `create_formatter()` simplifica a criação de objetos formatadores. Ela cuida dos detalhes de criar o objeto certo com base no nome do formato, para que os usuários não precisem se preocupar com isso.

Ao usar esses princípios orientados a objetos, criamos um sistema flexível e extensível para formatar dados tabulares em vários formatos de saída.
