# Gerar um Sinal

Vamos gerar um sinal e visualizá-lo usando Matplotlib.

```python
resolution = 1024
subsampling = 3  # fator de subamostragem
width = 100
n_components = resolution // subsampling

# Gerar um sinal
y = np.linspace(0, resolution - 1, resolution)
primeiro_quarto = y < resolution / 4
y[primeiro_quarto] = 3.0
y[np.logical_not(primeiro_quarto)] = -1.0

# Visualizar o sinal
plt.figure()
plt.plot(y)
plt.title("Sinal Original")
plt.show()
```
