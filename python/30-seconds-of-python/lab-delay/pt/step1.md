# Execução de Função Atrasada

Escreva uma função `delay(fn, ms, *args)` que recebe uma função `fn`, um tempo em milissegundos `ms` e qualquer número de argumentos `args`. A função deve atrasar a execução de `fn` por `ms` milissegundos e, em seguida, invocá-la com os argumentos fornecidos. A função deve retornar o resultado da invocação de `fn`.

Para atrasar a execução de `fn`, use a função `time.sleep()`. Esta função recebe um número de segundos como argumento, pelo que precisará de converter `ms` em segundos antes de passá-lo para `time.sleep()`.

```python
from time import sleep

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
```

```python
delay(lambda x: print(x), 1000, 'later') # prints 'later' after one second
```
