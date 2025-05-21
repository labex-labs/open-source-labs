# Implementando o Logging

Nesta etapa, vamos melhorar seu código. Em vez de usar mensagens de impressão simples, usaremos o módulo `logging` do Python para um logging (registro) adequado. O logging é uma ótima maneira de acompanhar o que seu programa está fazendo, especialmente quando se trata de lidar com erros e entender o fluxo do seu código.

## Compreendendo o Módulo Logging

O módulo `logging` em Python nos dá uma maneira flexível de enviar mensagens de log de nossos aplicativos. É muito mais poderoso do que apenas usar instruções de impressão simples. Veja o que ele pode fazer:

1. Diferentes níveis de log (DEBUG, INFO, WARNING, ERROR, CRITICAL): Esses níveis nos ajudam a categorizar a importância das mensagens. Por exemplo, DEBUG é para informações detalhadas que são úteis durante o desenvolvimento, enquanto CRITICAL é para erros graves que podem interromper o programa.
2. Formato de saída configurável: Podemos decidir como as mensagens de log serão exibidas, como adicionar timestamps ou outras informações úteis.
3. As mensagens podem ser direcionadas para diferentes saídas (console, arquivos, etc.): Podemos optar por mostrar as mensagens de log no console, salvá-las em um arquivo ou até mesmo enviá-las para um servidor remoto.
4. Filtragem de log com base na severidade: Podemos controlar quais mensagens vemos com base em seu nível de log.

## Adicionando Logging a reader.py

Agora, vamos alterar seu código para usar o módulo logging. Abra o arquivo `reader.py`.

Primeiro, precisamos importar o módulo `logging` e configurar um logger para este módulo. Adicione o seguinte código no topo do arquivo:

```python
import logging

# Set up a logger for this module
logger = logging.getLogger(__name__)
```

A instrução `import logging` traz o módulo `logging` para que possamos usar suas funções. O `logging.getLogger(__name__)` cria um logger para este módulo específico. Usar `__name__` garante que o logger tenha um nome exclusivo relacionado ao módulo.

Em seguida, modificaremos a função `convert_csv()` para usar o logging em vez de instruções de impressão. Aqui está o código atualizado:

```python
def convert_csv(rows, converter, header=True):
    """
    Convert a sequence of rows to an output sequence according to a conversion function.
    """
    if header:
        headers = next(rows)
    else:
        headers = []

    result = []
    for row_idx, row in enumerate(rows, start=1):
        try:
            # Try to convert the row
            result.append(converter(headers, row))
        except Exception as e:
            # Log a warning message for bad rows
            logger.warning(f"Row {row_idx}: Bad row: {row}")
            # Log the reason at debug level
            logger.debug(f"Row {row_idx}: Reason: {str(e)}")
            continue

    return result
```

As principais mudanças aqui são:

- Substituímos `print()` por `logger.warning()` para a mensagem de erro. Dessa forma, a mensagem é registrada com o nível de aviso apropriado, e podemos controlar sua visibilidade posteriormente.
- Adicionamos uma nova mensagem `logger.debug()` com detalhes sobre a exceção. Isso nos dá mais informações sobre o que deu errado, mas só é exibido se o nível de logging estiver definido como DEBUG ou inferior.
- O `str(e)` converte a exceção em uma string, para que possamos exibir o motivo do erro na mensagem de log.

Depois de fazer essas alterações, salve o arquivo.

## Testando o Logging

Vamos testar seu código com o logging habilitado. Abra o interpretador Python executando o seguinte comando em seu terminal:

```bash
python3
```

Depois de estar no interpretador Python, execute o seguinte código:

```python
import logging
import reader

# Configure logging level to see all messages
logging.basicConfig(level=logging.DEBUG)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

Aqui, primeiro importamos o módulo `logging` e nosso módulo `reader`. Em seguida, definimos o nível de logging como DEBUG usando `logging.basicConfig(level=logging.DEBUG)`. Isso significa que veremos todas as mensagens de log, incluindo DEBUG, INFO, WARNING, ERROR e CRITICAL. Em seguida, chamamos a função `read_csv_as_dicts` do módulo `reader` e imprimimos o número de linhas válidas processadas.

Você deve ver uma saída como esta:

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
DEBUG:reader:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
DEBUG:reader:Row 7: Reason: could not convert string to float: 'N/A'
...
Number of valid rows processed: 20
```

Observe que o módulo logging adiciona um prefixo a cada mensagem, mostrando o nível de log (WARNING/DEBUG) e o nome do módulo.

Agora, vamos ver o que acontece se mudarmos o nível de log para mostrar apenas avisos. Execute o seguinte código no interpretador Python:

```python
# Reset the logging configuration
import logging
logging.basicConfig(level=logging.WARNING)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
```

Desta vez, definimos o nível de logging como WARNING usando `logging.basicConfig(level=logging.WARNING)`. Agora você verá apenas as mensagens WARNING, e as mensagens DEBUG serão ocultas:

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
...
```

Isso mostra a vantagem de usar diferentes níveis de logging. Podemos controlar quantos detalhes são mostrados nos logs sem alterar nosso código.

Para sair do interpretador Python, execute o seguinte comando:

```python
exit()
```

Parabéns! Você agora implementou o tratamento de exceções e o logging adequados em seu programa Python. Isso torna seu código mais confiável e fornece melhores informações quando ocorrem erros.
