# Criar dados

Crie um array de valores entre 0 e 15 em incrementos de 0.01 e converta-os para radianos usando a função `radians` do pacote `basic_units`.

```python
from basic_units import radians
x = [val*radians for val in np.arange(0, 15, 0.01)]
```
