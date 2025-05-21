# Implementando a Validação de Tipo com Anotações de Função

Em Python, você tem a capacidade de adicionar anotações de tipo aos parâmetros de função. Essas anotações servem como uma maneira de indicar os tipos de dados esperados dos parâmetros e o valor de retorno de uma função. Elas não impõem os tipos em tempo de execução por padrão, mas podem ser usadas para fins de validação.

Vamos dar uma olhada em um exemplo:

```python
def add(x: int, y: int) -> int:
    return x + y
```

Neste código, `x: int` e `y: int` nos dizem que os parâmetros `x` e `y` devem ser inteiros. O `-> int` no final indica que a função `add` retorna um inteiro. Essas anotações de tipo são armazenadas no atributo `__annotations__` da função, que é um dicionário que mapeia nomes de parâmetros para seus tipos anotados.

Agora, vamos aprimorar nossa classe `ValidatedFunction` para usar essas anotações de tipo para validação. Para fazer isso, precisaremos usar o módulo `inspect` do Python. Este módulo fornece funções úteis para obter informações sobre objetos ativos, como módulos, classes, métodos, funções, etc. Em nosso caso, usaremos para corresponder os argumentos da função com seus nomes de parâmetros correspondentes.

Primeiro, precisamos modificar a classe `ValidatedFunction` no arquivo `validate.py`. Você pode abrir este arquivo usando o seguinte comando:

```bash
code /home/labex/project/validate.py
```

Substitua a classe `ValidatedFunction` existente pela seguinte versão aprimorada:

```python
import inspect

class ValidatedFunction:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __call__(self, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(*args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(*args, **kwargs)
```

Aqui está o que esta versão aprimorada faz:

1. Ele usa `inspect.signature()` para obter informações sobre os parâmetros da função, como seus nomes, valores padrão e tipos anotados.
2. O método `bind()` da assinatura é usado para corresponder os argumentos fornecidos aos seus nomes de parâmetros correspondentes. Isso nos ajuda a associar cada argumento ao seu parâmetro correto na função.
3. Ele verifica cada argumento em relação à sua anotação de tipo (se existir). Se uma anotação for encontrada, ele recupera a classe validadora da anotação e aplica a validação usando o método `check()`.
4. Finalmente, ele chama a função original com os argumentos validados.

Agora, vamos testar esta classe `ValidatedFunction` aprimorada com algumas funções que usam nossas classes validadoras em suas anotações de tipo. Abra o arquivo `test_validation.py` usando o seguinte comando:

```bash
code /home/labex/project/test_validation.py
```

Adicione o seguinte código ao arquivo:

```python
from validate import ValidatedFunction, Integer, String

def greet(name: String, times: Integer):
    return name * times

# Wrap the greet function with ValidatedFunction
validated_greet = ValidatedFunction(greet)

# Valid call
try:
    result = validated_greet("Hello ", 3)
    print(f"Valid call result: {result}")
except TypeError as e:
    print(f"Unexpected error: {e}")

# Invalid call - wrong type for 'name'
try:
    result = validated_greet(123, 3)
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for name: {e}")

# Invalid call - wrong type for 'times'
try:
    result = validated_greet("Hello ", "3")
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for times: {e}")
```

Neste código, definimos uma função `greet` com anotações de tipo `name: String` e `times: Integer`. Isso significa que o parâmetro `name` deve ser validado usando a classe `String` e o parâmetro `times` deve ser validado usando a classe `Integer`. Em seguida, envolvemos a função `greet` com nossa classe `ValidatedFunction` para habilitar a validação de tipo.

Realizamos três casos de teste: uma chamada válida, uma chamada inválida com o tipo errado para `name` e uma chamada inválida com o tipo errado para `times`. Cada chamada é envolvida em um bloco `try-except` para capturar quaisquer exceções `TypeError` que possam ser levantadas durante a validação.

Para executar o arquivo de teste, use o seguinte comando:

```bash
python3 /home/labex/project/test_validation.py
```

Você deve ver uma saída semelhante à seguinte:

```
Valid call result: Hello Hello Hello
Expected error for name: Expected <class 'str'>
Expected error for times: Expected <class 'int'>
```

Esta saída demonstra que nosso objeto chamável `ValidatedFunction` agora está aplicando a validação de tipo com base nas anotações da função. Quando passamos argumentos do tipo errado, as classes validadoras detectam o erro e levantam um `TypeError`. Dessa forma, podemos garantir que as funções sejam chamadas com os tipos de dados corretos, o que ajuda a evitar bugs e torna nosso código mais robusto.
