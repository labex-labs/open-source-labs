# Criar a Função Emitter

A função `emitter` gera os dados que serão passados para o método `update`. Neste caso, estamos gerando dados aleatórios com uma probabilidade de 0.1.

```python
def emitter(p=0.1):
    while True:
        v = np.random.rand()
        if v > p:
            yield 0.
        else:
            yield np.random.rand()
```
