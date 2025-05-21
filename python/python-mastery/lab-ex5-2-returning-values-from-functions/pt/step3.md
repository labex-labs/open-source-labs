# Trabalhando com Futures para Programação Concorrente

Em Python, quando você precisa executar funções ao mesmo tempo, ou concorrentemente, a linguagem oferece ferramentas úteis como threads e processos. Mas aqui está um problema comum que você enfrentará: como você pode obter o valor que uma função retorna quando ela está sendo executada em uma thread diferente? É aqui que o conceito de um `Future` se torna muito importante.

Um `Future` é como um espaço reservado para um resultado que estará disponível mais tarde. É uma maneira de representar um valor que uma função produzirá no futuro, mesmo antes que a função termine de ser executada. Vamos entender melhor esse conceito com um exemplo simples.

### Passo 1: Crie um Novo Arquivo

Primeiro, você precisa criar um novo arquivo Python. Vamos chamá-lo de `futures_demo.py`. Você pode usar o seguinte comando em seu terminal para criar este arquivo:

```
touch ~/project/futures_demo.py
```

### Passo 2: Adicione o Código da Função Básica

Agora, abra o arquivo `futures_demo.py` e adicione o seguinte código Python. Este código define uma função simples e mostra como uma chamada de função normal funciona.

```python
import time
import threading
from concurrent.futures import Future, ThreadPoolExecutor

def worker(x, y):
    """A function that takes time to complete"""
    print('Starting work...')
    time.sleep(5)  # Simulate a time-consuming task
    print('Work completed')
    return x + y

# Part 1: Normal function call
print("--- Part 1: Normal function call ---")
result = worker(2, 3)
print(f"Result: {result}")
```

Neste código, a função `worker` recebe dois números, os soma, mas primeiro simula uma tarefa demorada, pausando por 5 segundos. Quando você chama esta função de maneira normal, o programa espera que a função termine e, em seguida, obtém o valor de retorno.

### Passo 3: Execute o Código Básico

Salve o arquivo e execute-o usando o seguinte comando em seu terminal:

```
python ~/project/futures_demo.py
```

Você deve ver a saída assim:

```
--- Part 1: Normal function call ---
Starting work...
Work completed
Result: 5
```

Isso mostra que uma chamada de função normal espera que a função termine e, em seguida, retorna o resultado.

### Passo 4: Execute a Função em uma Thread Separada

Em seguida, vamos ver o que acontece quando executamos a função `worker` em uma thread separada. Adicione o seguinte código ao arquivo `futures_demo.py`:

```python
# Part 2: Running in a separate thread (problem: no way to get result)
print("\n--- Part 2: Running in a separate thread ---")
t = threading.Thread(target=worker, args=(2, 3))
t.start()
print("Main thread continues while worker runs...")
t.join()  # Wait for the thread to complete
print("Worker thread finished, but we don't have its return value!")
```

Aqui, estamos usando a classe `threading.Thread` para iniciar a função `worker` em uma nova thread. A thread principal não espera que a função `worker` termine e continua sua execução. No entanto, quando a thread `worker` termina, não temos uma maneira fácil de obter o valor de retorno.

### Passo 5: Execute o Código Threaded

Salve o arquivo novamente e execute-o usando o mesmo comando:

```
python ~/project/futures_demo.py
```

Você notará que a thread principal continua, a thread worker é executada, mas não podemos acessar o valor de retorno da função `worker`.

### Passo 6: Use um `Future` Manualmente

Para resolver o problema de obter o valor de retorno de uma thread, podemos usar um objeto `Future`. Adicione o seguinte código ao arquivo `futures_demo.py`:

```python
# Part 3: Using a Future to get the result
print("\n--- Part 3: Using a Future manually ---")

def do_work_with_future(x, y, future):
    """Wrapper that sets the result in the Future"""
    result = worker(x, y)
    future.set_result(result)

# Create a Future object
fut = Future()

# Start a thread that will set the result in the Future
t = threading.Thread(target=do_work_with_future, args=(2, 3, fut))
t.start()

print("Main thread continues...")
print("Waiting for the result...")
# Block until the result is available
result = fut.result()  # This will wait until set_result is called
print(f"Got the result: {result}")
```

Neste código, criamos um objeto `Future` e o passamos para uma nova função `do_work_with_future`. Esta função chama a função `worker` e, em seguida, define o resultado no objeto `Future`. A thread principal pode então usar o método `result()` do objeto `Future` para obter o resultado quando ele estiver disponível.

### Passo 7: Execute o Código com `Future`

Salve o arquivo e execute-o novamente:

```
python ~/project/futures_demo.py
```

Agora você verá que podemos obter com sucesso o valor de retorno da função em execução na thread.

### Passo 8: Use `ThreadPoolExecutor`

A classe `ThreadPoolExecutor` em Python torna o trabalho com tarefas concorrentes ainda mais fácil. Adicione o seguinte código ao arquivo `futures_demo.py`:

```python
# Part 4: Using ThreadPoolExecutor (easier way)
print("\n--- Part 4: Using ThreadPoolExecutor ---")
with ThreadPoolExecutor() as executor:
    # Submit the work to the executor
    future = executor.submit(worker, 2, 3)

    print("Main thread continues after submitting work...")
    print("Checking if the future is done:", future.done())

    # Get the result (will wait if not ready)
    result = future.result()
    print("Now the future is done:", future.done())
    print(f"Final result: {result}")
```

O `ThreadPoolExecutor` cuida de criar e gerenciar os objetos `Future` para você. Você só precisa enviar a função e seus argumentos, e ele retornará um objeto `Future` que você pode usar para obter o resultado.

### Passo 9: Execute o Código Completo

Salve o arquivo pela última vez e execute-o:

```
python ~/project/futures_demo.py
```

### Explicação

1.  **Chamada de Função Normal**: Quando você chama uma função da maneira normal, o programa espera que a função termine e obtém diretamente o valor de retorno.
2.  **Problema da Thread**: Executar uma função em uma thread separada tem uma desvantagem. Não há uma maneira integrada de obter o valor de retorno da função em execução nessa thread.
3.  **Future Manual**: Ao criar um objeto `Future` e passá-lo para a thread, podemos definir o resultado no `Future` e, em seguida, obter o resultado da thread principal.
4.  **ThreadPoolExecutor**: Esta classe simplifica a programação concorrente. Ele lida com a criação e o gerenciamento de objetos `Future` para você, tornando mais fácil executar funções concorrentemente e obter seus valores de retorno.

Objetos `Future` têm vários métodos úteis:

- `result()`: Este método é usado para obter o resultado da função. Se o resultado ainda não estiver pronto, ele esperará até que esteja.
- `done()`: Você pode usar este método para verificar se a computação da função foi concluída.
- `add_done_callback()`: Este método permite que você registre uma função que será chamada quando o resultado estiver pronto.

Este padrão é muito importante na programação concorrente, especialmente quando você precisa obter resultados de funções em execução em paralelo.
