# Configurar Parâmetros

Em seguida, definiremos os parâmetros para nossa simulação. Esses parâmetros incluem a aceleração devido à gravidade, o comprimento e a massa de cada pêndulo e o intervalo de tempo para a simulação.

```python
G = 9.8  # aceleração devido à gravidade, em m/s^2
L1 = 1.0  # comprimento do pêndulo 1 em m
L2 = 1.0  # comprimento do pêndulo 2 em m
L = L1 + L2  # comprimento máximo do pêndulo combinado
M1 = 1.0  # massa do pêndulo 1 em kg
M2 = 1.0  # massa do pêndulo 2 em kg
t_stop = 2.5  # quantos segundos simular
history_len = 500  # quantos pontos de trajetória exibir
```
