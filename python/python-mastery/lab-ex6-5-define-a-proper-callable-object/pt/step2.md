# Criando um Objeto Chamável Básico

Em Python, um objeto chamável (callable object) é um objeto que pode ser usado como uma função. Você pode pensar nisso como algo que você pode "chamar" colocando parênteses depois dele, semelhante a como você chama uma função regular. Para fazer com que uma classe em Python aja como um objeto chamável, precisamos implementar um método especial chamado `__call__`. Este método é invocado automaticamente quando você usa o objeto com parênteses, assim como quando você chama uma função.

Vamos começar modificando o arquivo `validate.py`. Vamos adicionar uma nova classe chamada `ValidatedFunction` a este arquivo, e esta classe será nosso objeto chamável. Para abrir o arquivo no editor de código, execute o seguinte comando no terminal:

```bash
code /home/labex/project/validate.py
```

Depois que o arquivo estiver aberto, role até o final dele e adicione o seguinte código:

```python
class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        result = self.func(*args, **kwargs)
        return result
```

Vamos detalhar o que este código faz. A classe `ValidatedFunction` tem um método `__init__`, que é o construtor. Quando você cria uma instância desta classe, você passa uma função para ela. Esta função é então armazenada como um atributo da instância, chamado `self.func`.

O método `__call__` é a parte chave que torna esta classe chamável. Quando você chama uma instância da classe `ValidatedFunction`, este método `__call__` é executado. Veja o que ele faz passo a passo:

1. Ele imprime uma mensagem que informa qual função está sendo chamada. Isso é útil para depuração e compreensão do que está acontecendo.
2. Ele chama a função que foi armazenada em `self.func` com os argumentos que você passou quando chamou a instância. `*args` e `**kwargs` permitem que você passe qualquer número de argumentos posicionais e de palavras-chave.
3. Ele retorna o resultado da chamada da função.

Agora, vamos testar esta classe `ValidatedFunction`. Criaremos um novo arquivo chamado `test_callable.py` para escrever nosso código de teste. Para abrir este novo arquivo no editor de código, execute o seguinte comando:

```bash
code /home/labex/project/test_callable.py
```

Adicione o seguinte código ao arquivo `test_callable.py`:

```python
from validate import ValidatedFunction

def add(x, y):
    return x + y

# Wrap the add function with ValidatedFunction
validated_add = ValidatedFunction(add)

# Call the wrapped function
result = validated_add(2, 3)
print(f"Result: {result}")

# Try another call
result = validated_add(10, 20)
print(f"Result: {result}")
```

Neste código, primeiro importamos a classe `ValidatedFunction` do arquivo `validate.py`. Em seguida, definimos uma função simples chamada `add` que recebe dois números e retorna sua soma.

Criamos uma instância da classe `ValidatedFunction`, passando a função `add` para ela. Isso "envolve" a função `add` dentro da instância `ValidatedFunction`.

Em seguida, chamamos a função envolvida duas vezes, uma vez com os argumentos `2` e `3`, e depois com `10` e `20`. Cada vez que chamamos a função envolvida, o método `__call__` da classe `ValidatedFunction` é invocado, que por sua vez chama a função `add` original.

Para executar o código de teste, execute o seguinte comando no terminal:

```bash
python3 /home/labex/project/test_callable.py
```

Você deve ver uma saída semelhante a esta:

```
Calling <function add at 0x7f2d1c3a9940>
Result: 5
Calling <function add at 0x7f2d1c3a9940>
Result: 30
```

Esta saída mostra que nosso objeto chamável está funcionando como esperado. Quando chamamos `validated_add(2, 3)`, na verdade estamos chamando o método `__call__` da classe `ValidatedFunction`, que então chama a função `add` original.

No momento, nossa classe `ValidatedFunction` apenas imprime uma mensagem e passa a chamada para a função original. Na próxima etapa, melhoraremos esta classe para realizar a validação de tipo com base nas anotações da função.
