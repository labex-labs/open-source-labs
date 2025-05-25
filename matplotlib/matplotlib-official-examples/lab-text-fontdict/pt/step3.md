# Criar o Gráfico

Agora, podemos criar nosso gráfico. Geraremos alguns dados usando NumPy e plotaremos uma curva de decaimento exponencial amortecido.

```python
x = np.linspace(0.0, 5.0, 100)
y = np.cos(2*np.pi*x) * np.exp(-x)

plt.plot(x, y, 'k')
```
