# Configurar as variáveis

Em seguida, configuraremos as variáveis para o nosso sinal. Usaremos um intervalo de amostragem de 0,01, o que nos dá uma frequência de amostragem de 100 Hz. Criaremos um array de tempo de 0 a 10 segundos com um passo de 0,01 segundos. Também geraremos ruído usando a função `randn` do NumPy e o convolucionaremos com uma função de decaimento exponencial para criar um sinal ruidoso.

```python
np.random.seed(0)

dt = 0.01  # intervalo de amostragem
Fs = 1 / dt  # frequência de amostragem
t = np.arange(0, 10, dt)

# gerar ruído:
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)
cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]

s = 0.1 * np.sin(4 * np.pi * t) + cnse  # o sinal
```
