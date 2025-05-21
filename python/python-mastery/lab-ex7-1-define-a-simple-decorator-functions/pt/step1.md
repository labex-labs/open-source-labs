# Criando Seu Primeiro Decorador

## O que são Decoradores?

Em Python, decoradores são uma sintaxe especial que pode ser bastante útil para iniciantes. Eles permitem que você modifique o comportamento de funções ou métodos. Pense em um decorador como uma função que recebe outra função como entrada. Em seguida, ele retorna uma nova função. Essa nova função geralmente estende ou altera o comportamento da função original.

Decoradores são aplicados usando o símbolo `@`. Você coloca este símbolo seguido pelo nome do decorador diretamente acima da definição de uma função. Esta é uma maneira simples de dizer ao Python que você deseja usar o decorador naquela função específica.

## Criando um Decorador de Logging Simples

Vamos criar um decorador simples que registra informações quando uma função é chamada. Logging (registro) é uma tarefa comum em aplicações do mundo real, e usar um decorador para isso é uma ótima maneira de entender como eles funcionam.

1. Primeiro, abra o editor VSCode. No diretório `/home/labex/project`, crie um novo arquivo chamado `logcall.py`. Este arquivo conterá nossa função decoradora.

2. Adicione o seguinte código a `logcall.py`:

```python
# logcall.py

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Vamos detalhar o que este código faz:

- A função `logged` é nosso decorador. Ele recebe outra função, que chamamos de `func`, como um argumento. Esta `func` é a função à qual queremos adicionar logging.
- Quando o decorador é aplicado a uma função, ele imprime uma mensagem. Esta mensagem nos diz que o logging está sendo adicionado à função com o nome fornecido.
- Dentro da função `logged`, definimos uma função interna chamada `wrapper`. Esta função `wrapper` é o que substituirá a função original.
  - Quando a função decorada é chamada, a função `wrapper` imprime uma mensagem dizendo que a função está sendo chamada.
  - Em seguida, ele chama a função original (`func`) com todos os argumentos que foram passados para ela. Os `*args` e `**kwargs` são usados para aceitar qualquer número de argumentos posicionais e de palavras-chave.
  - Finalmente, ele retorna o resultado da função original.
- A função `logged` retorna a função `wrapper`. Esta função `wrapper` agora será usada em vez da função original, adicionando a funcionalidade de logging.

## Usando o Decorador

3. Agora, no mesmo diretório (`/home/labex/project`), crie outro arquivo chamado `sample.py` com o seguinte código:

```python
# sample.py

from logcall import logged

@logged
def add(x, y):
    return x + y

@logged
def sub(x, y):
    return x - y
```

A sintaxe `@logged` é muito importante aqui. Ela diz ao Python para aplicar o decorador `logged` às funções `add` e `sub`. Portanto, sempre que essas funções forem chamadas, a funcionalidade de logging adicionada pelo decorador será executada.

## Testando o Decorador

4. Para testar seu decorador, abra um terminal no VSCode. Primeiro, altere o diretório para o diretório do projeto usando o seguinte comando:

```bash
cd /home/labex/project
```

Em seguida, inicie o interpretador Python:

```bash
python3
```

5. No interpretador Python, importe o módulo `sample` e teste as funções decoradas:

```python
>>> import sample
Adding logging to add
Adding logging to sub
>>> sample.add(3, 4)
Calling add
7
>>> sample.sub(2, 3)
Calling sub
-1
>>> exit()
```

Observe que, ao importar o módulo `sample`, as mensagens "Adding logging to..." são impressas. Isso ocorre porque o decorador é aplicado quando o módulo é importado. Cada vez que você chama uma das funções decoradas, a mensagem "Calling..." é impressa. Isso mostra que o decorador está funcionando como esperado.

Este decorador simples demonstra o conceito básico de decoradores. Ele envolve a função original com funcionalidade adicional (logging neste caso) sem alterar o código da função original. Este é um recurso poderoso em Python que você pode usar em muitos cenários diferentes.
