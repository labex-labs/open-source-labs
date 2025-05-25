# O Depurador Python

Você pode iniciar manualmente o depurador dentro de um programa.

```python
def some_function():
    ...
    breakpoint()      # Enter the debugger (Python 3.7+)
    ...
```

Isso inicia o depurador na chamada `breakpoint()`.

Em versões anteriores do Python, você fazia isso. Você às vezes verá isso mencionado em outros guias de depuração.

```python
import pdb
...
pdb.set_trace()       # Instead of `breakpoint()`
...
```
