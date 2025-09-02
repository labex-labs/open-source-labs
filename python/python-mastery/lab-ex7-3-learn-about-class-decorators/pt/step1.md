# Implementando Verificação de Tipo com Descritores

Nesta etapa, vamos criar uma classe `Stock` que utiliza descritores para verificação de tipo. Mas primeiro, vamos entender o que são descritores. Descritores são um recurso realmente poderoso em Python. Eles lhe dão controle sobre como os atributos são acessados nas classes.

Descritores são objetos que definem como os atributos são acessados em outros objetos. Eles fazem isso implementando métodos especiais como `__get__`, `__set__` e `__delete__`. Esses métodos permitem que os descritores gerenciem como os atributos são recuperados, definidos e excluídos. Descritores são muito úteis para implementar validação, verificação de tipo e propriedades computadas. Por exemplo, você pode usar um descritor para garantir que um atributo seja sempre um número positivo ou uma string de um determinado formato.

O arquivo `validate.py` já possui classes validadoras (`String`, `PositiveInteger`, `PositiveFloat`). Podemos usar essas classes para validar os atributos da nossa classe `Stock`.

Agora, vamos criar nossa classe `Stock` com descritores.

1. Primeiro, abra o arquivo `stock.py` no seu editor.

2. Assim que o arquivo estiver aberto, substitua o conteúdo placeholder pelo seguinte código:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

# Create an __init__ method based on _fields
Stock.create_init()
```

Vamos analisar o que este código faz. A tupla `_fields` define os atributos da classe `Stock`. Estes são os nomes dos atributos que nossos objetos `Stock` terão.

Os atributos `name`, `shares` e `price` são definidos como objetos descritores. O descritor `String()` garante que o atributo `name` seja uma string. O descritor `PositiveInteger()` garante que o atributo `shares` seja um inteiro positivo. E o descritor `PositiveFloat()` garante que o atributo `price` seja um número de ponto flutuante positivo.

A propriedade `cost` é uma propriedade computada. Ela calcula o custo total do estoque com base no número de ações e no preço por ação.

O método `sell` é usado para reduzir o número de ações. Quando você chama este método com um número de ações para vender, ele subtrai esse número do atributo `shares`.

A linha `Stock.create_init()` cria dinamicamente um método `__init__` para nossa classe. Este método nos permite criar objetos `Stock` passando os valores para os atributos `name`, `shares` e `price`.

3. Após adicionar o código, salve o arquivo. Isso garantirá que suas alterações sejam salvas e possam ser usadas ao executar os testes.

4. Agora, vamos executar os testes para verificar sua implementação. Primeiro, mude o diretório para o diretório `~/project` executando o seguinte comando:

```bash
cd ~/project
```

Em seguida, execute os testes usando o seguinte comando:

```bash
python3 teststock.py
```

Se sua implementação estiver correta, você deverá ver uma saída semelhante a esta:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Esta saída significa que todos os testes estão passando. Os descritores estão validando com sucesso os tipos de cada atributo!

Vamos tentar criar um objeto `Stock` no interpretador Python. Primeiro, certifique-se de estar no diretório `~/project`. Em seguida, execute o seguinte comando:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Você deverá ver a seguinte saída:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Você implementou com sucesso descritores para verificação de tipo! Agora, vamos melhorar ainda mais este código.
