# Radianos para Graus

Escreva uma função Python chamada `rads_to_degrees` que recebe um único argumento `rad`, que é um número de ponto flutuante (float) representando um ângulo em radianos. A função deve retornar o ângulo em graus como um número de ponto flutuante. Você pode usar a seguinte fórmula para converter um ângulo de radianos para graus:

```
degrees = radians * (180 / pi)
```

onde `pi` é um valor constante que representa a razão entre a circunferência de um círculo e seu diâmetro, que é aproximadamente igual a 3.14159.

Sua função deve importar a constante `pi` do módulo `math`.

```python
from math import pi

def rads_to_degrees(rad):
  return (rad * 180.0) / pi
```

```python
from math import pi

rads_to_degrees(pi / 2) # 90.0
```
