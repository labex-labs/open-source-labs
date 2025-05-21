# Testando Nosso Agendador de Tarefas

Agora, vamos adicionar um teste ao nosso arquivo `multitask.py`. O objetivo deste teste é executar múltiplas tarefas ao mesmo tempo, o que é conhecido como execução concorrente. A execução concorrente permite que diferentes tarefas progridam aparentemente ao mesmo tempo, embora em um ambiente de thread único, as tarefas realmente se revezem para executar.

Para realizar este teste, adicione o seguinte código ao final do arquivo `multitask.py`:

```python
# Test our scheduler
if __name__ == '__main__':
    # Add tasks to the queue
    tasks.append(countdown(10))  # Count down from 10
    tasks.append(countdown(5))   # Count down from 5
    tasks.append(countup(20))    # Count up to 20

    # Run all tasks
    run()
```

Neste código, primeiro verificamos se o script está sendo executado diretamente usando `if __name__ == '__main__':`. Em seguida, adicionamos três tarefas diferentes à fila `tasks`. As tarefas `countdown` contarão regressivamente a partir dos números fornecidos, e a tarefa `countup` contará até o número especificado. Finalmente, chamamos a função `run()` para começar a executar essas tarefas.

Após adicionar o código, execute-o com o seguinte comando no terminal:

```bash
python3 /home/labex/project/multitask.py
```

Quando você executar o código, deverá ver uma saída semelhante a esta (a ordem exata das linhas pode variar):

```
T-minus 10
T-minus 5
Up we go 0
T-minus 9
T-minus 4
Up we go 1
T-minus 8
T-minus 3
Up we go 2
...
```

Observe como a saída das diferentes tarefas é misturada. Esta é uma clara indicação de que nosso agendador está executando todas as três tarefas concorrentemente. Cada vez que uma tarefa atinge uma instrução `yield`, o agendador pausa essa tarefa e muda para outra, permitindo que todas as tarefas progridam ao longo do tempo.

## Como Funciona

Vamos dar uma olhada mais de perto no que acontece quando nosso agendador é executado:

1. Primeiro, adicionamos três tarefas geradoras à fila: `countdown(10)`, `countdown(5)` e `countup(20)`. Essas tarefas geradoras são funções especiais que podem pausar e retomar sua execução nas instruções `yield`.
2. Em seguida, a função `run()` inicia seu trabalho:
   - Ele pega a primeira tarefa, `countdown(10)`, da fila.
   - Ele executa esta tarefa até que ela atinja uma instrução `yield`. Quando atinge o `yield`, ele imprime "T-minus 10".
   - Depois disso, ele adiciona a tarefa `countdown(10)` de volta à fila para que ela possa ser executada novamente mais tarde.
   - Em seguida, ele pega a tarefa `countdown(5)` da fila.
   - Ele executa a tarefa `countdown(5)` até que ela atinja uma instrução `yield`, imprimindo "T-minus 5".
   - E este processo continua...

Este ciclo continua até que todas as tarefas sejam concluídas. Cada tarefa tem a chance de ser executada por um curto período, o que dá a ilusão de execução concorrente sem a necessidade de usar threads ou callbacks. Threads são uma maneira mais complexa de alcançar a concorrência, e callbacks são usados em programação assíncrona. Nosso agendador simples usa geradores para obter um efeito semelhante de uma maneira mais direta.
