# Compreendendo Variáveis de Classe e Métodos de Classe

Neste primeiro passo, vamos mergulhar nos conceitos de variáveis de classe e métodos de classe em Python. Estes são conceitos importantes que o ajudarão a escrever um código mais eficiente e organizado. Antes de começarmos a trabalhar com variáveis de classe e métodos de classe, vamos primeiro dar uma olhada em como as instâncias da nossa classe `Stock` são criadas atualmente. Isso nos dará uma compreensão básica e nos mostrará onde podemos fazer melhorias.

## O que são Variáveis de Classe?

Variáveis de classe são um tipo especial de variáveis em Python. Elas são compartilhadas entre todas as instâncias de uma classe. Para entender melhor isso, vamos compará-las com variáveis de instância. Variáveis de instância são exclusivas para cada instância de uma classe. Por exemplo, se você tiver várias instâncias de uma classe, cada instância pode ter seu próprio valor para uma variável de instância. Por outro lado, as variáveis de classe são definidas no nível da classe. Isso significa que todas as instâncias dessa classe podem acessar e compartilhar o mesmo valor da variável de classe.

## O que são Métodos de Classe?

Métodos de classe são métodos que funcionam na própria classe, não em instâncias individuais da classe. Eles estão vinculados à classe, o que significa que podem ser chamados diretamente na classe sem criar uma instância. Para definir um método de classe em Python, usamos o decorador `@classmethod`. E, em vez de receber a instância (`self`) como o primeiro parâmetro, os métodos de classe recebem a classe (`cls`) como seu primeiro parâmetro. Isso permite que eles operem em dados no nível da classe e executem ações relacionadas à classe como um todo.

## Abordagem Atual para Criar Instâncias de Stock

Vamos primeiro ver como criamos atualmente instâncias da classe `Stock`. Abra o arquivo `stock.py` no editor para observar a implementação atual:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
```

As instâncias desta classe são normalmente criadas de uma destas maneiras:

1. Inicialização direta com valores:

   ```python
   s = Stock('GOOG', 100, 490.1)
   ```

   Aqui, estamos criando diretamente uma instância da classe `Stock` fornecendo os valores para os atributos `name`, `shares` e `price`. Esta é uma maneira direta de criar uma instância quando você conhece os valores antecipadamente.

2. Criação a partir de dados lidos de um arquivo CSV:
   ```python
   import csv
   with open('portfolio.csv') as f:
       rows = csv.reader(f)
       headers = next(rows)  # Skip the header
       row = next(rows)      # Get the first data row
       s = Stock(row[0], int(row[1]), float(row[2]))
   ```
   Quando lemos dados de um arquivo CSV, os valores estão inicialmente em formato de string. Portanto, ao criar uma instância de `Stock` a partir de dados CSV, precisamos converter manualmente os valores de string para os tipos apropriados. Por exemplo, o valor `shares` precisa ser convertido em um inteiro, e o valor `price` precisa ser convertido em um float.

Vamos experimentar isso. Crie um novo arquivo Python chamado `test_stock.py` no diretório `~/project` com o seguinte conteúdo:

```python
# test_stock.py
from stock import Stock
import csv

# Method 1: Direct creation
s1 = Stock('GOOG', 100, 490.1)
print(f"Stock: {s1.name}, Shares: {s1.shares}, Price: {s1.price}")
print(f"Cost: {s1.cost()}")

# Method 2: Creation from CSV row
with open('portfolio.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Skip the header
    row = next(rows)      # Get the first data row
    s2 = Stock(row[0], int(row[1]), float(row[2]))
    print(f"\nStock from CSV: {s2.name}, Shares: {s2.shares}, Price: {s2.price}")
    print(f"Cost: {s2.cost()}")
```

Execute este arquivo para ver os resultados:

```bash
cd ~/project
python test_stock.py
```

Você deve ver uma saída semelhante a:

```
Stock: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0

Stock from CSV: AA, Shares: 100, Price: 32.2
Cost: 3220.0
```

Esta conversão manual funciona, mas tem algumas desvantagens. Precisamos saber o formato exato dos dados e temos que realizar as conversões toda vez que criamos uma instância a partir de dados CSV. Isso pode ser propenso a erros e demorado. No próximo passo, criaremos uma solução mais elegante usando métodos de classe.
