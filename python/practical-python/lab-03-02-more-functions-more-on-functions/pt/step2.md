# Argumentos Padrão (Default Arguments)

Às vezes, você deseja que um argumento seja opcional. Se for o caso, atribua um valor padrão na definição da função.

```python
def read_prices(filename, debug=False):
    ...
```

Se um valor padrão for atribuído, o argumento é opcional nas chamadas de função.

```python
d = read_prices('prices.csv')
e = read_prices('prices.dat', True)
```

_Nota: Argumentos com valores padrão devem aparecer no final da lista de argumentos (todos os argumentos não opcionais vêm primeiro)._
