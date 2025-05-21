# Entendendo o Problema

Antes de começarmos a explorar metaclasses, é importante entender o problema que pretendemos resolver. Em programação, frequentemente precisamos criar estruturas com tipos específicos para seus atributos. Em nosso trabalho anterior, desenvolvemos um sistema para estruturas com verificação de tipos. Este sistema nos permite definir classes onde cada atributo tem um tipo específico, e os valores atribuídos a esses atributos são validados de acordo com esse tipo.

Aqui está um exemplo de como usamos este sistema para criar uma classe `Stock`:

```python
from validate import String, PositiveInteger, PositiveFloat
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

Neste código, primeiro importamos os tipos de validadores (`String`, `PositiveInteger`, `PositiveFloat`) do módulo `validate` e a classe `Structure` do módulo `structure`. Em seguida, definimos a classe `Stock`, que herda de `Structure`. Dentro da classe `Stock`, definimos atributos com tipos de validadores específicos. Por exemplo, o atributo `name` deve ser uma string, `shares` deve ser um inteiro positivo e `price` deve ser um float positivo.

No entanto, há um problema com essa abordagem. Precisamos importar todos os tipos de validadores no topo do nosso arquivo. À medida que adicionamos mais e mais tipos de validadores em um cenário do mundo real, essas importações podem se tornar muito longas e difíceis de gerenciar. Isso pode nos levar a usar `from validate import *`, o que geralmente é considerado uma má prática porque pode causar conflitos de nomes e tornar o código menos legível.

Para entender nosso ponto de partida, vamos dar uma olhada na classe `Structure`. Você precisa abrir o arquivo `structure.py` no editor e examinar seu conteúdo. Isso ajudará você a ver como o tratamento da estrutura básica é implementado antes de adicionarmos a funcionalidade de metaclasse.

```bash
code structure.py
```

Ao abrir o arquivo, você verá uma implementação básica da classe `Structure`. Esta classe é responsável por lidar com a inicialização de atributos, mas ainda não possui nenhuma funcionalidade de metaclasse.

Em seguida, vamos examinar as classes de validadores. Essas classes são definidas no arquivo `validate.py`. Elas já possuem funcionalidade de descritor, o que significa que podem controlar como os atributos são acessados e definidos. Mas precisaremos aprimorá-las para resolver o problema de importação que discutimos anteriormente.

```bash
code validate.py
```

Ao olhar para essas classes de validadores, você terá uma melhor compreensão de como o processo de validação funciona e quais alterações precisamos fazer para melhorar nosso código.
