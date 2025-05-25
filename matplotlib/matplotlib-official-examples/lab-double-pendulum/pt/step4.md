# Configurar as Condições Iniciais e Integrar a EDO

Agora, configuraremos as condições iniciais para nossa simulação. Definiremos os ângulos e as velocidades angulares iniciais de cada pêndulo, bem como o intervalo de tempo para a simulação. Em seguida, integraremos a EDO (Equação Diferencial Ordinária - ODE) usando o método de Euler para obter a posição e a velocidade de cada pêndulo em cada passo de tempo.

```python
# criar um array de tempo de 0..t_stop amostrado em passos de 0.02 segundos
dt = 0.01
t = np.arange(0, t_stop, dt)

# th1 e th2 são os ângulos iniciais (graus)
# w10 e w20 são as velocidades angulares iniciais (graus por segundo)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# estado inicial
state = np.radians([th1, w1, th2, w2])

# integrar a EDO usando o método de Euler
y = np.empty((len(t), 4))
y[0] = state
for i in range(1, len(t)):
    y[i] = y[i - 1] + derivs(t[i - 1], y[i - 1]) * dt
```
