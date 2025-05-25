# Gerar os cantos dos retângulos

Para desenhar nosso histograma usando retângulos, precisamos calcular os cantos de cada retângulo. Adicione o seguinte código:

```python
left = bins[:-1]
right = bins[1:]
bottom = np.zeros(len(left))
top = bottom + n
```
