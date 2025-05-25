# Graus para Radianos

Escreva uma função `degrees_to_rads(deg)` que recebe um ângulo em graus como argumento e retorna o ângulo em radianos. Sua função deve usar a seguinte fórmula para converter graus em radianos:

```
radians = (degrees * pi) / 180.0
```

onde `pi` é um valor constante que representa a razão entre a circunferência de um círculo e seu diâmetro (aproximadamente 3.14159).

Sua função deve retornar o ângulo em radianos arredondado para 4 casas decimais.

```python
from math import pi

def degrees_to_rads(deg):
  return (deg * pi) / 180.0
```

```python
degrees_to_rads(180) # ~3.1416
```
