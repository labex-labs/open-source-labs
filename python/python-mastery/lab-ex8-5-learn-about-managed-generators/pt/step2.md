# Criando um Agendador de Tarefas com Geradores

Em programação, um agendador de tarefas é uma ferramenta crucial que ajuda a gerenciar e executar múltiplas tarefas de forma eficiente. Nesta seção, usaremos geradores para construir um agendador de tarefas simples que pode executar múltiplas funções geradoras simultaneamente. Isso mostrará como os geradores podem ser gerenciados para realizar multitarefa cooperativa, o que significa que as tarefas se revezam para executar e compartilhar o tempo de execução.

Primeiro, você precisa criar um novo arquivo. Navegue até o diretório `/home/labex/project` e crie um arquivo chamado `multitask.py`. Este arquivo conterá o código para nosso agendador de tarefas.

```python
# multitask.py

from collections import deque

# Task queue
tasks = deque()

# Simple task scheduler
def run():
    while tasks:
        task = tasks.popleft()  # Get the next task
        try:
            task.send(None)     # Resume the task
            tasks.append(task)  # Put it back in the queue
        except StopIteration:
            print('Task done')  # Task is complete

# Example task 1: Countdown
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield              # Pause execution
        n -= 1

# Example task 2: Count up
def countup(n):
    x = 0
    while x < n:
        print('Up we go', x)
        yield              # Pause execution
        x += 1
```

Agora, vamos detalhar como este agendador de tarefas funciona:

1. Usamos um `deque` (fila de duas extremidades) para armazenar nossas tarefas geradoras. Um `deque` é uma estrutura de dados que permite adicionar e remover elementos de ambas as extremidades de forma eficiente. É uma ótima escolha para nossa fila de tarefas porque precisamos adicionar tarefas ao final e removê-las do início.
2. A função `run()` é o coração do nosso agendador de tarefas. Ele pega tarefas da fila uma por uma:
   - Ele retoma cada tarefa usando `send(None)`. Isso é semelhante a usar `next()` em um gerador. Ele diz ao gerador para continuar a execução de onde parou.
   - Após a tarefa produzir (yield), ela é adicionada de volta ao final da fila. Dessa forma, a tarefa terá outra chance de ser executada mais tarde.
   - Quando uma tarefa é concluída (levanta `StopIteration`), ela é removida da fila. Isso indica que a tarefa terminou sua execução.
3. Cada instrução `yield` em nossas tarefas geradoras age como um ponto de pausa. Quando um gerador atinge uma instrução `yield`, ele pausa sua execução e devolve o controle ao agendador. Isso permite que outras tarefas sejam executadas.

Essa abordagem implementa multitarefa cooperativa. Cada tarefa voluntariamente cede o controle de volta ao agendador, permitindo que outras tarefas sejam executadas. Dessa forma, múltiplas tarefas podem compartilhar o tempo de execução e serem executadas simultaneamente.
