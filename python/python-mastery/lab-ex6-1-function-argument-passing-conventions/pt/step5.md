# Reescrevendo a Classe Stock

Agora que temos uma classe base `Structure` bem definida, é hora de reescrever nossa classe `Stock`. Ao usar esta classe base, podemos simplificar nosso código e torná-lo mais organizado. A classe `Structure` fornece um conjunto de funcionalidades comuns que podemos reutilizar em nossa classe `Stock`, o que é uma grande vantagem para a manutenibilidade e legibilidade do código.

## Criando a Nova Classe Stock

Vamos começar criando um novo arquivo chamado `stock.py`. Este arquivo conterá nossa classe `Stock` reescrita. Aqui está o código que você precisa colocar no arquivo `stock.py`:

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        """
        Calculate the cost as shares * price
        """
        return self.shares * self.price

    def sell(self, nshares):
        """
        Sell a number of shares
        """
        self.shares -= nshares
```

Vamos detalhar o que esta nova classe `Stock` faz:

1.  Ela herda da classe `Structure`. Isso significa que a classe `Stock` pode usar todos os recursos fornecidos pela classe `Structure`. Um dos benefícios é que não precisamos escrever um método `__init__` nós mesmos, porque a classe `Structure` cuida da atribuição de atributos automaticamente.
2.  Definimos `_fields`, que é uma tupla que especifica os atributos da classe `Stock`. Esses atributos são `name`, `shares` e `price`.
3.  A propriedade `cost` é definida para calcular o custo total da ação. Ela multiplica o número de `shares` pelo `price`.
4.  O método `sell` é usado para reduzir o número de ações. Quando você chama este método com um número de ações para vender, ele subtrai esse número do número atual de ações.

## Testando a Nova Classe Stock

Para garantir que nossa nova classe `Stock` funcione conforme o esperado, precisamos criar um arquivo de teste. Vamos criar um arquivo chamado `test_stock.py` com o seguinte código:

```python
# test_stock.py
from stock import Stock

# Create a stock
s = Stock('GOOG', 100, 490.1)

# Check the attributes
print(f"Stock: {s}")
print(f"Name: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost}")

# Sell some shares
print("\nSelling 20 shares...")
s.sell(20)
print(f"Shares after selling: {s.shares}")
print(f"Cost after selling: {s.cost}")

# Try to set an invalid attribute
print("\nTrying to set an invalid attribute:")
try:
    s.prices = 500  # Invalid attribute (should be 'price')
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

Neste arquivo de teste, primeiro importamos a classe `Stock` do arquivo `stock.py`. Em seguida, criamos uma instância da classe `Stock` com o nome 'GOOG', 100 ações e um preço de 490,1. Imprimimos os atributos da ação para verificar se eles estão definidos corretamente. Depois disso, vendemos 20 ações e imprimimos o novo número de ações e o novo custo. Finalmente, tentamos definir um atributo inválido `prices` (deveria ser `price`). Se nossa classe `Stock` estiver funcionando corretamente, ela deverá gerar um `AttributeError`.

Para executar o teste, abra seu terminal e digite o seguinte comando:

```bash
python3 test_stock.py
```

A saída esperada é a seguinte:

```
Stock: Stock('GOOG', 100, 490.1)
Name: GOOG
Shares: 100
Price: 490.1
Cost: 49010.0

Selling 20 shares...
Shares after selling: 80
Cost after selling: 39208.0

Trying to set an invalid attribute:
Error correctly caught: No attribute prices
```

## Executando Testes de Unidade

Se você tiver testes de unidade de exercícios anteriores, poderá executá-los em sua nova implementação. Em seu terminal, digite o seguinte comando:

```bash
python3 teststock.py
```

Observe que alguns testes podem falhar. Isso pode ser porque eles esperam comportamentos ou métodos específicos que ainda não implementamos. Não se preocupe com isso! Continuaremos a construir sobre essa base em exercícios futuros.

## Revisão de Nosso Progresso

Vamos dedicar um momento para revisar o que alcançamos até agora:

1.  Criamos uma classe base `Structure` reutilizável. Esta classe:
    - Lida automaticamente com a atribuição de atributos, o que nos poupa de escrever muito código repetitivo.
    - Fornece uma boa representação de string, tornando mais fácil imprimir e depurar nossos objetos.
    - Restringe os nomes dos atributos para evitar erros, o que torna nosso código mais robusto.

2.  Reescrevemos nossa classe `Stock`. Ela:
    - Hereda da classe `Structure` para reutilizar a funcionalidade comum.
    - Define apenas os campos e métodos específicos do domínio, o que mantém a classe focada e limpa.
    - Tem um design claro e simples, tornando-o fácil de entender e manter.

Essa abordagem tem vários benefícios para nosso código:

- É mais sustentável porque temos menos repetição. Se precisarmos alterar algo na funcionalidade comum, só precisamos alterá-lo na classe `Structure`.
- É mais robusto por causa da melhor verificação de erros fornecida pela classe `Structure`.
- É mais legível porque as responsabilidades de cada classe são claras.

Em exercícios futuros, continuaremos a construir sobre essa base para criar um sistema de gerenciamento de portfólio de ações mais sofisticado.
