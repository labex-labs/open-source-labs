# Lista Unfold (Desdobramento de Lista)

Sua tarefa é implementar a função `unfold` que recebe uma função iteradora e um valor inicial (seed) como argumentos. A função iteradora aceita um argumento (`seed`) e deve sempre retornar uma lista com dois elementos ([`value`, `nextSeed`]) ou `False` para terminar. A função `unfold` deve usar uma função geradora (generator function), `fn_generator`, que usa um loop `while` para chamar a função iteradora e `yield` o `value` até que retorne `False`. Finalmente, a função `unfold` deve usar uma compreensão de lista (list comprehension) para retornar a lista produzida pelo gerador, usando a função iteradora.

Implemente a função `unfold`:

```python
def unfold(fn, seed):
    # your code here
```

### Entrada (Input)

- Uma função iteradora `fn` que aceita um argumento (`seed`) e deve sempre retornar uma lista com dois elementos ([`value`, `nextSeed`]) ou `False` para terminar.
- Um valor inicial (seed) `seed`.

### Saída (Output)

- Uma lista que é produzida pelo gerador, usando a função iteradora.

```python
def unfold(fn, seed):
  def fn_generator(val):
    while True:
      val = fn(val[1])
      if val == False: break
      yield val[0]
  return [i for i in fn_generator([None, seed])]
```

```python
f = lambda n: False if n > 50 else [-n, n + 10]
unfold(f, 10) # [-10, -20, -30, -40, -50]
```
