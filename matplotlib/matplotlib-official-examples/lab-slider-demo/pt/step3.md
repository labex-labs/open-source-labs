# Criar o Gráfico Inicial

Agora, criaremos o gráfico inicial da onda senoidal. Definiremos os parâmetros iniciais para a amplitude e frequência e plotaremos a onda senoidal usando esses parâmetros.

```python
t = np.linspace(0, 1, 1000)
init_amplitude = 5
init_frequency = 3

fig, ax = plt.subplots()
line, = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
ax.set_xlabel('Time [s]')
```
