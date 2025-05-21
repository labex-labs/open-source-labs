# Coletando Tipos de Validadores

Em Python, validadores são classes que nos ajudam a garantir que os dados atendam a certos critérios. Nossa primeira tarefa neste experimento é modificar a classe base `Validator` para que ela possa coletar todas as suas subclasses. Por que precisamos fazer isso? Bem, ao coletar todas as subclasses de validadores, podemos criar um namespace que contém todos os tipos de validadores. Mais tarde, injetaremos este namespace na classe `Structure`, o que facilitará o gerenciamento e o uso de diferentes validadores.

Agora, vamos começar a trabalhar no código. Abra o arquivo `validate.py`. Você pode usar o seguinte comando no terminal para abri-lo:

```bash
code validate.py
```

Depois que o arquivo estiver aberto, precisamos adicionar um dicionário em nível de classe e um método `__init_subclass__()` à classe `Validator`. O dicionário em nível de classe será usado para armazenar todas as subclasses de validadores, e o método `__init_subclass__()` é um método especial em Python que é chamado toda vez que uma subclasse da classe atual é definida.

Adicione o seguinte código à classe `Validator`, logo após a definição da classe:

```python
# Adicione isso à classe Validator em validate.py
validators = {}  # Dicionário para coletar todas as subclasses de validadores

@classmethod
def __init_subclass__(cls):
    """Registra cada subclasse de validador no dicionário de validadores"""
    Validator.validators[cls.__name__] = cls
```

Depois de adicionar o código, sua classe `Validator` modificada agora deve se parecer com isto:

```python
class Validator:
    validators = {}  # Dicionário para coletar todas as subclasses de validadores

    @classmethod
    def __init_subclass__(cls):
        """Registra cada subclasse de validador no dicionário de validadores"""
        Validator.validators[cls.__name__] = cls

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    def validate(self, value):
        pass
```

Agora, toda vez que um novo tipo de validador é definido, como `String` ou `PositiveInteger`, o Python chamará automaticamente o método `__init_subclass__()`. Este método, então, adicionará a nova subclasse de validador ao dicionário `validators`, usando o nome da classe como chave.

Vamos testar se nosso código funciona. Criaremos um script Python simples para verificar o conteúdo do dicionário `validators`. Você pode executar o seguinte comando no terminal:

```bash
python3 -c "from validate import Validator; print(Validator.validators)"
```

Se tudo funcionar corretamente, você deverá ver uma saída semelhante a esta, mostrando todos os tipos de validadores e suas classes correspondentes:

```
{'Typed': <class 'validate.Typed'>, 'Positive': <class 'validate.Positive'>, 'NonEmpty': <class 'validate.NonEmpty'>, 'String': <class 'validate.String'>, 'Integer': <class 'validate.Integer'>, 'Float': <class 'validate.Float'>, 'PositiveInteger': <class 'validate.PositiveInteger'>, 'PositiveFloat': <class 'validate.PositiveFloat'>, 'NonEmptyString': <class 'validate.NonEmptyString'>}
```

Agora que temos um dicionário contendo todos os nossos tipos de validadores, podemos usá-lo na próxima etapa para criar nossa metaclasse.
