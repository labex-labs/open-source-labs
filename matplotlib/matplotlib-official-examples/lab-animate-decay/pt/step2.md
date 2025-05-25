# Criar a função geradora de dados

Em seguida, precisamos criar uma função para gerar os dados para a animação. A função produzirá uma onda senoidal que decai ao longo do tempo. Usaremos a função `itertools.count()` para gerar uma sequência infinita de números. Usaremos esses números para calcular os valores da onda senoidal.

```python
def data_gen():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
```
