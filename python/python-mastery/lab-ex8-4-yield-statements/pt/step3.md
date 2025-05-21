# Aplicações Práticas do Gerenciamento de Geradores

Nesta etapa, vamos explorar como aplicar os conceitos que aprendemos sobre o gerenciamento de geradores e o tratamento de exceções em geradores a cenários do mundo real. Compreender essas aplicações práticas o ajudará a escrever um código Python mais robusto e eficiente.

## Criando um Sistema Robusto de Monitoramento de Arquivos

Vamos construir uma versão mais confiável do nosso sistema de monitoramento de arquivos. Este sistema será capaz de lidar com diferentes situações, como timeouts e solicitações do usuário para parar.

Primeiro, abra o editor WebIDE e crie um novo arquivo chamado `robust_follow.py`. Aqui está o código que você precisa escrever neste arquivo:

```python
import os
import time
import signal

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

def follow(filename, timeout=None):
    """
    A generator that yields new lines in a file.
    With timeout handling and proper cleanup.
    """
    try:
        # Set up timeout if specified
        if timeout:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout)

        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    # No new data, wait briefly
                    time.sleep(0.1)
                    continue
                yield line
    except TimeoutError:
        print(f"Following timed out after {timeout} seconds")
    except GeneratorExit:
        print("Following stopped by request")
    finally:
        # Clean up timeout alarm if it was set
        if timeout:
            signal.alarm(0)
        print("Follow generator cleanup complete")
```

Neste código, primeiro definimos uma classe `TimeoutError` personalizada. A função `timeout_handler` é usada para lançar esse erro quando ocorre um timeout. A função `follow` é um gerador que lê um arquivo e produz novas linhas. Se um timeout for especificado, ele configura um alarme usando o módulo `signal`. Se não houver novos dados no arquivo, ele espera por um curto período de tempo antes de tentar novamente. O bloco `try - except - finally` é usado para lidar com diferentes exceções e garantir a limpeza adequada.

Após escrever o código, salve o arquivo.

## Experimentando com o Sistema Robusto de Monitoramento de Arquivos

Agora, vamos testar nosso sistema de monitoramento de arquivos aprimorado. Abra um terminal e execute o interpretador Python com os seguintes comandos:

```bash
cd ~/project
python3
```

### Experimento 1: Uso Básico

No interpretador Python, testaremos a funcionalidade básica do nosso gerador `follow`. Aqui está o código a ser executado:

```python
>>> from robust_follow import follow
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 2:  # Just read a few lines for the example
...         break
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Line 3: "HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
```

Aqui, importamos a função `follow` do nosso arquivo `robust_follow.py`. Em seguida, criamos um objeto gerador `f` que acompanha o arquivo `stocklog.csv`. Usamos um loop `for` para iterar sobre as linhas produzidas pelo gerador e imprimir as três primeiras linhas.

### Experimento 2: Usando Timeout

Vamos ver como o recurso de timeout funciona. Execute o seguinte código no interpretador Python:

```python
>>> # Create a generator that will time out after 3 seconds
>>> f = follow('stocklog.csv', timeout=3)
>>> for line in f:
...     print(line.strip())
...     time.sleep(1)  # Process each line slowly
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
Following timed out after 3 seconds
Follow generator cleanup complete
```

Neste experimento, criamos um gerador com um timeout de 3 segundos. Processamos cada linha lentamente, dormindo por 1 segundo entre cada linha. Após cerca de 3 segundos, o gerador lança uma exceção de timeout, e o código de limpeza no bloco `finally` é executado.

### Experimento 3: Fechamento Explícito

Vamos testar como o gerador lida com um fechamento explícito. Execute o seguinte código:

```python
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 1:
...         print("Explicitly closing the generator...")
...         f.close()
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Explicitly closing the generator...
Following stopped by request
Follow generator cleanup complete
```

Aqui, criamos um gerador e começamos a iterar sobre suas linhas. Após processar duas linhas, fechamos explicitamente o gerador usando o método `close`. O gerador então lida com a exceção `GeneratorExit` e realiza a limpeza necessária.

## Criando um Pipeline de Processamento de Dados com Tratamento de Erros

Em seguida, criaremos um pipeline de processamento de dados simples usando corrotinas. Este pipeline será capaz de lidar com erros em diferentes estágios.

Abra o editor WebIDE e crie um novo arquivo chamado `pipeline.py`. Aqui está o código para escrever neste arquivo:

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def grep(pattern, target):
    """Filter lines containing pattern and send to target"""
    try:
        while True:
            line = yield
            if pattern in line:
                target.send(line)
    except Exception as e:
        target.throw(e)

@consumer
def printer():
    """Print received items"""
    try:
        while True:
            item = yield
            print(f"PRINTER: {item}")
    except Exception as e:
        print(f"PRINTER ERROR: {repr(e)}")

def follow_and_process(filename, pattern):
    """Follow a file and process its contents"""
    import time
    import os

    output = printer()
    filter_pipe = grep(pattern, output)

    try:
        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                filter_pipe.send(line)
    except KeyboardInterrupt:
        print("Processing stopped by user")
    finally:
        filter_pipe.close()
        output.close()
```

Neste código, o decorador `consumer` é usado para inicializar corrotinas. A corrotina `grep` filtra as linhas que contêm um padrão específico e as envia para outra corrotina. A corrotina `printer` imprime os itens recebidos. A função `follow_and_process` lê um arquivo, filtra suas linhas usando a corrotina `grep` e imprime as linhas correspondentes usando a corrotina `printer`. Ele também lida com a exceção `KeyboardInterrupt` e garante a limpeza adequada.

Após escrever o código, salve o arquivo.

## Testando o Pipeline de Processamento de Dados

Vamos testar nosso pipeline de processamento de dados. Em um terminal, execute o seguinte comando:

```bash
cd ~/project
python3 -c "from pipeline import follow_and_process; follow_and_process('stocklog.csv', 'IBM')"
```

Você deve ver uma saída semelhante a esta:

```
PRINTER: "IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550

PRINTER: "IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859

PRINTER: "IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
```

Esta saída mostra que o pipeline está funcionando corretamente, filtrando e imprimindo linhas que contêm o padrão "IBM".

Para interromper o processo, pressione `Ctrl+C`. Você deve ver a seguinte mensagem:

```
Processing stopped by user
```

## Principais Conclusões

1. O tratamento adequado de exceções em geradores permite que você crie sistemas robustos que podem lidar com erros de forma elegante. Isso significa que seus programas não travarão inesperadamente quando algo der errado.
2. Você pode usar técnicas como timeouts para evitar que os geradores sejam executados indefinidamente. Isso ajuda a gerenciar os recursos do sistema e garante que seu programa não fique preso em um loop infinito.
3. Geradores e corrotinas podem formar pipelines de processamento de dados poderosos, onde os erros podem ser propagados e tratados no nível apropriado. Isso facilita a construção de sistemas complexos de processamento de dados.
4. O bloco `finally` em geradores garante que as operações de limpeza sejam executadas, independentemente de como o gerador termina. Isso ajuda a manter a integridade do seu programa e evita vazamentos de recursos.
