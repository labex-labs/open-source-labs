# Mapear Número para Intervalo

Escreva uma função chamada `num_to_range` que recebe cinco argumentos: `num`, `inMin`, `inMax`, `outMin` e `outMax`. A função deve retornar `num` mapeado entre `outMin`-`outMax` a partir de `inMin`-`inMax`. Em outras palavras, a função deve pegar um número (`num`) que se enquadra em um determinado intervalo (`inMin`-`inMax`) e mapeá-lo para um novo intervalo (`outMin`-`outMax`).

```python
def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax
                  - outMin))
```

```python
num_to_range(5, 0, 10, 0, 100) # 50.0
```
