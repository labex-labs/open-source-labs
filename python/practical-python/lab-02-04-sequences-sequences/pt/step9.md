# Função enumerate()

A função `enumerate` adiciona um valor de contador extra à iteração.

```python
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    # Loops with i = 0, name = 'Elwood'
    # i = 1, name = 'Jake'
    # i = 2, name = 'Curtis'
```

A forma geral é `enumerate(sequence [, start = 0])`. `start` é opcional. Um bom exemplo de uso de `enumerate()` é rastrear números de linha ao ler um arquivo:

```python
with open(filename) as f:
    for lineno, line in enumerate(f, start=1):
        ...
```

No final, `enumerate` é apenas um atalho útil para:

```python
i = 0
for x in s:
    statements
    i += 1
```

Usar `enumerate` exige menos digitação e roda um pouco mais rápido.
