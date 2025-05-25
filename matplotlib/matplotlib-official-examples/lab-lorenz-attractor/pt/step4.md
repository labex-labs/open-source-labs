# Calcular o Atrator de Lorenz

Calculamos o Atrator de Lorenz avançando no tempo e estimando o próximo ponto usando o ponto anterior e a função Lorenz.

```python
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt
```
