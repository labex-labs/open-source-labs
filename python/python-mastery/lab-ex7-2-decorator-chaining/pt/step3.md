# Aplicando Decoradores a Métodos de Classe

Agora, vamos explorar como os _decorators_ interagem com métodos de classe. Isso pode ser um pouco complicado porque o Python tem diferentes tipos de métodos: métodos de instância, métodos de classe, métodos estáticos e propriedades. _Decorators_ são funções que recebem outra função e estendem o comportamento da última função sem modificá-la explicitamente. Ao aplicar _decorators_ a métodos de classe, precisamos prestar atenção em como eles funcionam com esses diferentes tipos de métodos.

## Entendendo o Desafio

Vamos ver o que acontece quando aplicamos nosso _decorator_ `@logged` a diferentes tipos de métodos. O _decorator_ `@logged` provavelmente é usado para registrar informações sobre as chamadas de método.

1. Crie um novo arquivo `methods.py` no WebIDE. Este arquivo conterá nossa classe com diferentes tipos de métodos decorados com o _decorator_ `@logged`.

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @logged
    @classmethod
    def class_method(cls):
        print("Class method called")
        return "class result"

    @logged
    @staticmethod
    def static_method():
        print("Static method called")
        return "static result"

    @logged
    @property
    def property_method(self):
        print("Property method called")
        return "property result"
```

Neste código, temos uma classe `Spam` com quatro tipos diferentes de métodos. Cada método é decorado com o _decorator_ `@logged`, e alguns também são decorados com outros _decorators_ embutidos como `@classmethod`, `@staticmethod` e `@property`.

2. Vamos testar como funciona. Executaremos um comando Python no terminal para chamar esses métodos e ver a saída.

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

Ao executar este comando, você pode notar alguns problemas:

- O _decorator_ `@property` pode não funcionar corretamente com nosso _decorator_ `@logged`. O _decorator_ `@property` é usado para definir um método como uma propriedade, e ele tem uma maneira específica de funcionar. Quando combinado com o _decorator_ `@logged`, pode haver conflitos.
- A ordem dos _decorators_ importa para `@classmethod` e `@staticmethod`. A ordem em que os _decorators_ são aplicados pode alterar o comportamento do método.

## A Ordem dos Decoradores

Ao aplicar vários _decorators_, eles são aplicados de baixo para cima. Isso significa que o _decorator_ mais próximo da definição do método é aplicado primeiro, e então os acima dele são aplicados em sequência. Por exemplo:

```python
@decorator1
@decorator2
def func():
    pass
```

Isso é equivalente a:

```python
func = decorator1(decorator2(func))
```

Neste exemplo, `decorator2` é aplicado a `func` primeiro, e então `decorator1` é aplicado ao resultado de `decorator2(func)`.

## Corrigindo a Ordem do Decorator

Vamos atualizar nosso arquivo `methods.py` para corrigir a ordem do _decorator_. Ao alterar a ordem dos _decorators_, podemos garantir que cada método funcione como esperado.

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @classmethod
    @logged
    def class_method(cls):
        print("Class method called")
        return "class result"

    @staticmethod
    @logged
    def static_method():
        print("Static method called")
        return "static result"

    @property
    @logged
    def property_method(self):
        print("Property method called")
        return "property result"
```

Nesta versão atualizada:

- Para `instance_method`, a ordem não importa. Métodos de instância são chamados em uma instância da classe, e o _decorator_ `@logged` pode ser aplicado em qualquer ordem sem afetar sua funcionalidade básica.
- Para `class_method`, aplicamos `@classmethod` após `@logged`. O _decorator_ `@classmethod` altera a maneira como o método é chamado, e aplicá-lo após `@logged` garante que o _logging_ funcione corretamente.
- Para `static_method`, aplicamos `@staticmethod` após `@logged`. Semelhante ao `@classmethod`, o _decorator_ `@staticmethod` tem seu próprio comportamento, e a ordem com o _decorator_ `@logged` precisa estar correta.
- Para `property_method`, aplicamos `@property` após `@logged`. Isso garante que o comportamento da propriedade seja mantido, além de obter a funcionalidade de _logging_.

3. Vamos testar o código atualizado. Executaremos o mesmo comando que antes para ver se os problemas foram corrigidos.

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

Você deve agora ver o _logging_ adequado para todos os tipos de métodos:

```
Calling instance_method
Instance method called
instance result
Calling class_method
Class method called
class result
Calling static_method
Static method called
static result
Calling property_method
Property method called
property result
```

## Melhores Práticas para Decoradores de Métodos

Ao trabalhar com _decorators_ de métodos, siga estas melhores práticas:

1. Aplique _decorators_ de transformação de método (`@classmethod`, `@staticmethod`, `@property`) **após** seus _decorators_ personalizados. Isso garante que os _decorators_ personalizados possam executar seu _logging_ ou outras operações primeiro, e então os _decorators_ embutidos podem transformar o método conforme o pretendido.
2. Esteja ciente de que a execução do _decorator_ ocorre no momento da definição da classe, não no momento da chamada do método. Isso significa que qualquer código de configuração ou inicialização no _decorator_ será executado quando a classe for definida, não quando o método for chamado.
3. Para casos mais complexos, você pode precisar criar _decorators_ especializados para diferentes tipos de métodos. Diferentes tipos de métodos têm comportamentos diferentes, e um _decorator_ único pode não funcionar em todas as situações.
