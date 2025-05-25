# Código que faz _logging_ (registro)

Talvez você possa criar uma função que cria funções com _logging_ (registro) adicionado a elas. Um _wrapper_ (envoltório).

```python
def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Agora use-o.

```python
def add(x, y):
    return x + y

logged_add = logged(add)
```

O que acontece quando você chama a função retornada por `logged`?

```python
logged_add(3, 4)      # Você vê a mensagem de logging aparecer
```

Este exemplo ilustra o processo de criação de uma chamada _função *wrapper* (envoltório)_.

Um _wrapper_ (envoltório) é uma função que envolve outra função com alguns pedaços extras de processamento, mas, de outra forma, funciona exatamente da mesma maneira que a função original.

```python
>>> logged_add(3, 4)
Calling add   # Saída extra. Adicionada pelo wrapper
7
>>>
```

_Nota: A função `logged()` cria o *wrapper* (envoltório) e o retorna como resultado._
