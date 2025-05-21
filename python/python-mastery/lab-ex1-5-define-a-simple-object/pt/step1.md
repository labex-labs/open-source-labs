# Entendendo Classes Python

Em Python, uma classe serve como um modelo para criar objetos. A programação orientada a objetos (POO) é uma abordagem poderosa que nos permite organizar nosso código de forma eficaz. Ela faz isso agrupando dados e funções relacionadas. Dessa forma, podemos gerenciar programas complexos com mais facilidade e tornar nosso código mais modular e sustentável.

Uma classe Python é composta por dois componentes principais:

- **Atributos (Attributes)**: São variáveis que armazenam dados dentro de uma classe. Pense nos atributos como as características ou propriedades de um objeto. Por exemplo, se estamos criando uma classe para representar uma pessoa, os atributos podem ser o nome, a idade e a altura da pessoa.
- **Métodos (Methods)**: São funções que pertencem a uma classe e podem acessar ou modificar seus atributos. Métodos definem as ações que um objeto pode realizar. Usando o exemplo da classe pessoa, um método pode ser uma função que calcula a idade da pessoa em meses.

Classes são extremamente úteis, pois fornecem uma maneira de criar código reutilizável e modelar conceitos do mundo real. Neste laboratório, criaremos uma classe `Stock`. Esta classe será usada para representar informações de ações, como o nome da ação, o número de ações e o preço por ação.

Aqui está a estrutura básica de uma classe Python:

```python
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

    def method_name(self):
        # Code that uses the attributes
        return result
```

O método `__init__` é um método especial em classes Python. Ele é chamado automaticamente quando criamos um novo objeto a partir da classe. Este método é usado para inicializar os atributos do objeto. O parâmetro `self` é uma referência à instância da classe. Ele é usado para acessar atributos e métodos de dentro da classe. Quando chamamos um método em um objeto, o Python automaticamente passa o próprio objeto como o primeiro argumento, e é por isso que usamos `self` nas definições dos métodos. Isso nos permite trabalhar com os atributos da instância específica e realizar operações neles.
