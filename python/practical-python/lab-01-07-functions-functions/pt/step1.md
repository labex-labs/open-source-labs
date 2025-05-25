# Funções Personalizadas

Use funções para código que você deseja reutilizar. Aqui está uma definição de função:

```python
def sumcount(n):
    '''
    Retorna a soma dos primeiros n inteiros
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total
```

Para chamar uma função:

```python
a = sumcount(100)
```

Uma função é uma série de instruções que executam alguma tarefa e retornam um resultado. A palavra-chave `return` é necessária para especificar explicitamente o valor de retorno da função.
